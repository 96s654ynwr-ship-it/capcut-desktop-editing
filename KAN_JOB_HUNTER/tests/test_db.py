import tempfile
import unittest
from pathlib import Path

from kan_job_hunter.db import Database


class DatabaseStateTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db = Database(Path(self.temp_dir.name) / "state.sqlite3")
        self.db.initialize()
        self.source_id = self.db.upsert_source({
            "telegram_id": 123,
            "username": "example",
            "title": "Example",
            "source_type": "channel",
            "relevance_score": 0.8,
            "languages": ["русский"],
        })

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_message_upsert_is_idempotent_and_notification_is_deduplicated(self):
        row = {
            "telegram_message_id": 77,
            "title": "Монтажёр",
            "description": "Ищем монтажёра",
            "match_score": 0.8,
            "raw_text": "Ищем монтажёра",
        }
        first = self.db.upsert_message(self.source_id, row)
        second = self.db.upsert_message(self.source_id, row)
        self.assertEqual(first, second)
        self.assertTrue(self.db.claim_notification(first))
        self.db.mark_notification_sent(first, 9001)
        self.assertFalse(self.db.claim_notification(first))

    def test_failed_notification_can_be_retried(self):
        row = {"telegram_message_id": 88, "description": "оператор", "match_score": 0.4, "raw_text": "оператор"}
        message_id = self.db.upsert_message(self.source_id, row)
        self.assertTrue(self.db.claim_notification(message_id))
        self.db.mark_notification_failed(message_id, "temporary")
        self.assertTrue(self.db.claim_notification(message_id))
