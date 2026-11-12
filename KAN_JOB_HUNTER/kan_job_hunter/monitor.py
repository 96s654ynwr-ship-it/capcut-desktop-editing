import asyncio
import logging
from telethon import TelegramClient

from .db import Database
from .filters import analyze_text, is_recent_publication, message_publication_datetime
from .notifier import Notifier

logger = logging.getLogger(__name__)


class Monitor:
    def __init__(self, client: TelegramClient, db: Database, notifier: Notifier | None, recent_limit: int = 30):
        self.client, self.db, self.notifier, self.recent_limit = client, db, notifier, recent_limit
        self.last_stats = {}

    def _reset_stats(self) -> None:
        self.last_stats = {
            "checked_messages": 0,
            "accepted_recent": 0,
            "discarded_no_text": 0,
            "discarded_unknown_date": 0,
            "discarded_stale": 0,
            "discarded_irrelevant": 0,
            "notifications_sent": 0,
            "notifications_failed": 0,
        }

    def sources(self) -> list[dict]:
        with self.db.connect() as c:
            return [dict(row) for row in c.execute("SELECT * FROM sources WHERE enabled=1 ORDER BY id")]

    async def check_source(self, source: dict) -> int:
        # A StringSession on a fresh runner may not contain the access hash for
        # an entity stored only by numeric ID. Public usernames are resolvable
        # without relying on the local entity cache.
        entity_ref = source.get("username") or source["telegram_id"]
        entity = await self.client.get_entity(entity_ref)
        newest = None; found = 0
        async for message in self.client.iter_messages(entity, limit=self.recent_limit):
            self.last_stats["checked_messages"] += 1
            newest = newest or message.id
            if not message.message:
                self.last_stats["discarded_no_text"] += 1
                continue
            publication_dt = message_publication_datetime(message)
            if publication_dt is None:
                self.last_stats["discarded_unknown_date"] += 1
                continue
            published_at = publication_dt.isoformat()
            if not is_recent_publication(published_at):
                self.last_stats["discarded_stale"] += 1
                continue
            analysis = analyze_text(message.message, published_at=published_at)
            if not analysis["relevant"]:
                self.last_stats["discarded_irrelevant"] += 1
                continue
            analysis.update({
                "telegram_message_id": int(message.id),
                "original_url": f"https://t.me/{source['username']}/{message.id}",
                "source_title": source["title"],
                "source_username": source.get("username"),
            })
            db_id = self.db.upsert_message(source["id"], analysis)
            found += 1
            self.last_stats["accepted_recent"] += 1
            self.db.log_action("message_detected", db_id, {"source": source["username"]})
            if self.notifier and self.db.claim_notification(db_id):
                try:
                    provider_message_id = await self.notifier.notify(analysis)
                    self.db.mark_notification_sent(db_id, provider_message_id)
                    self.last_stats["notifications_sent"] += 1
                except Exception as error:
                    self.db.mark_notification_failed(db_id, type(error).__name__)
                    self.last_stats["notifications_failed"] += 1
                    logger.warning("Notification failed: %s", type(error).__name__)
        self.db.mark_checked(source["telegram_id"], newest)
        return found

    async def run_once(self) -> int:
        self._reset_stats()
        total = 0
        for source in self.sources():
            try:
                total += await self.check_source(source)
            except Exception as error:
                logger.warning("Source %s failed: %s", source.get("username"), type(error).__name__)
        return total

    async def loop(self, interval: int) -> None:
        while True:
            await self.run_once()
            await asyncio.sleep(interval)
