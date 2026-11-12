import asyncio
import logging
from datetime import datetime, timezone

from telethon import TelegramClient

from .db import Database
from .filters import analyze_text
from .notifier import Notifier

logger = logging.getLogger(__name__)


class Monitor:
    def __init__(self, client: TelegramClient, db: Database, notifier: Notifier | None, recent_limit: int = 30):
        self.client, self.db, self.notifier, self.recent_limit = client, db, notifier, recent_limit

    def sources(self) -> list[dict]:
        with self.db.connect() as c:
            return [dict(row) for row in c.execute("SELECT * FROM sources WHERE enabled=1 ORDER BY id")]

    async def check_source(self, source: dict) -> int:
        entity = await self.client.get_entity(source["telegram_id"])
        newest = None; found = 0
        async for message in self.client.iter_messages(entity, limit=self.recent_limit):
            newest = newest or message.id
            if not message.message:
                continue
            analysis = analyze_text(message.message, published_at=message.date.isoformat() if message.date else None)
            if not analysis["relevant"]:
                continue
            analysis.update({
                "telegram_message_id": int(message.id),
                "original_url": f"https://t.me/{source['username']}/{message.id}",
            })
            db_id = self.db.upsert_message(source["id"], analysis)
            found += 1
            self.db.log_action("message_detected", db_id, {"source": source["username"]})
            if self.notifier and self.db.claim_notification(db_id):
                try:
                    provider_message_id = await self.notifier.notify(analysis)
                    self.db.mark_notification_sent(db_id, provider_message_id)
                except Exception as error:
                    self.db.mark_notification_failed(db_id, type(error).__name__)
                    logger.warning("Notification failed: %s", type(error).__name__)
        self.db.mark_checked(source["telegram_id"], newest)
        return found

    async def run_once(self) -> int:
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
