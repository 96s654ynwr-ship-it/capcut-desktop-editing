import argparse
import asyncio
import logging

from telethon import TelegramClient
from telethon.sessions import StringSession

from .config import get_settings
from .db import Database
from .discovery import DiscoveryService
from .logging_setup import configure_logging
from .monitor import Monitor
from .notifier import Notifier


def build_user_client(settings):
    session = StringSession(settings.telegram_session_string) if settings.telegram_session_string else str(settings.session_path)
    return TelegramClient(session, settings.telegram_api_id, settings.telegram_api_hash, request_retries=2)


async def connect_user(client, non_interactive: bool) -> None:
    if non_interactive:
        await client.connect()
        if not await client.is_user_authorized():
            raise RuntimeError("TELEGRAM_SESSION_STRING/session is not authorized")
    else:
        await client.start()


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="kan-job-hunter")
    s = p.add_subparsers(dest="command", required=True)
    s.add_parser("init", help="Initialize SQLite")
    s.add_parser("auth", help="Authorize the local Telegram user session")
    s.add_parser("export-session", help="Export the authorized local session to an ignored file")
    for name, help_text in [("discover", "Discover public sources without joining"), ("check", "Check monitored sources once"), ("run", "Discover periodically and monitor periodically")]:
        sub = s.add_parser(name, help=help_text)
        sub.add_argument("--non-interactive", action="store_true", help="Fail instead of asking for login input")
    s.add_parser("health", help="Validate local database and runtime health")
    return p


async def auth(settings, db):
    settings.validate_user()
    async with TelegramClient(str(settings.session_path), settings.telegram_api_id, settings.telegram_api_hash) as client:
        await client.start()
        print("Telegram user session authorized locally.")


async def worker(command: str, non_interactive: bool = False) -> None:
    settings = get_settings()
    db = Database(settings.db_path)
    db.initialize()
    if command == "init":
        print(f"SQLite initialized: {settings.db_path}")
        return
    if command == "health":
        with db.connect() as connection:
            connection.execute("SELECT 1").fetchone()
        print("healthy")
        return
    settings.validate_user()
    user = build_user_client(settings)
    await connect_user(user, non_interactive)
    try:
        if command == "discover":
            count = await DiscoveryService(user, db, settings.discovery_limit_per_query, settings.recent_messages_per_source).discover()
            print(f"Discovered/updated sources: {count}")
            return
        notifier = Notifier(settings.bot_token, settings.notification_chat_id) if settings.bot_token and settings.notification_chat_id is not None else None
        monitor = Monitor(user, db, notifier, settings.recent_messages_per_source)
        if command == "check":
            accepted = await monitor.run_once()
            stats = monitor.last_stats
            print(
                f"Checked messages: {stats['checked_messages']}; "
                f"relevant in last 72h: {accepted}; "
                f"no-text discarded: {stats['discarded_no_text']}; "
                f"stale discarded: {stats['discarded_stale']}; "
                f"unknown-date discarded: {stats['discarded_unknown_date']}; "
                f"irrelevant discarded: {stats['discarded_irrelevant']}; "
                f"notifications sent: {stats['notifications_sent']}; "
                f"notification failures: {stats['notifications_failed']}"
            )
            return
        discovery = DiscoveryService(user, db, settings.discovery_limit_per_query, settings.recent_messages_per_source)
        last_discovery = 0.0
        while True:
            now = asyncio.get_running_loop().time()
            if now - last_discovery >= settings.discovery_interval_seconds:
                await discovery.discover()
                last_discovery = now
            await monitor.run_once()
            await asyncio.sleep(settings.poll_interval_seconds)
    finally:
        await user.disconnect()


def main() -> None:
    settings = get_settings(); configure_logging(settings.logs_path, settings.log_level)
    args = parser().parse_args()
    try:
        if args.command == "auth":
            asyncio.run(auth(settings, Database(settings.db_path)))
        elif args.command == "export-session":
            from .export_session import main as export_session
            asyncio.run(export_session())
        else:
            asyncio.run(worker(args.command, getattr(args, "non_interactive", False)))
    except KeyboardInterrupt: print("Stopped.")
    except Exception as error: raise SystemExit(f"Error: {error}") from error
