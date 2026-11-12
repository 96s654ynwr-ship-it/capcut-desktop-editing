import logging
from datetime import datetime

from telethon import TelegramClient, types
from telethon.tl import functions

from .db import Database
from .filters import analyze_text, discovery_queries

logger = logging.getLogger(__name__)


class DiscoveryService:
    def __init__(self, client: TelegramClient, db: Database, limit: int = 20, recent_limit: int = 30):
        self.client, self.db, self.limit, self.recent_limit = client, db, limit, recent_limit

    async def discover(self) -> int:
        added = 0
        for query in discovery_queries():
            try:
                result = await self.client(functions.contacts.SearchRequest(q=query, limit=self.limit))
                for entity in result.chats:
                    if not isinstance(entity, types.Channel) or not getattr(entity, "username", None):
                        continue
                    sample = []
                    async for message in self.client.iter_messages(entity, limit=self.recent_limit):
                        if message.message:
                            sample.append(message.message)
                    analysis = analyze_text("\n".join(sample))
                    if not analysis["relevant"]:
                        continue
                    row = {
                        "telegram_id": int(entity.id),
                        "username": entity.username,
                        "title": entity.title,
                        "source_type": "channel" if getattr(entity, "broadcast", False) else "group",
                        "relevance_score": analysis["match_score"],
                        "languages": [analysis["language"]] if analysis["language"] != "не указан" else [],
                    }
                    self.db.upsert_source(row)
                    added += 1
            except Exception as error:
                logger.warning("Discovery query failed: %s", type(error).__name__)
        return added
