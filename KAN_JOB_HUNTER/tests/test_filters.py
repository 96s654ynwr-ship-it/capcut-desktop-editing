import unittest
from datetime import datetime, timedelta, timezone

from kan_job_hunter.filters import analyze_text, is_recent_publication, message_publication_datetime


class FilterTests(unittest.TestCase):
    NOW = datetime(2026, 11, 12, 12, 0, tzinfo=timezone.utc)

    def test_madrid_russian_editor_with_payment(self):
        row = analyze_text("Ищем видеомонтажёра в Мадриде. Оплата 800 €. Работа на русском.")
        self.assertTrue(row["relevant"])
        self.assertEqual(row["city"], "Мадрид")
        self.assertEqual(row["language"], "русский")
        self.assertEqual(row["payment"], "800 €")

    def test_ai_and_motion_are_excluded(self):
        row = analyze_text("Ищем AI-креатора и motion designer для рекламы")
        self.assertFalse(row["relevant"])

    def test_unknown_data_is_not_invented(self):
        row = analyze_text("Нужен оператор для проекта")
        self.assertEqual(row["payment"], None)
        self.assertEqual(row["contact"], None)

    def test_publication_from_2022_is_rejected(self):
        self.assertFalse(is_recent_publication("2022-06-01T10:00:00+00:00", now=self.NOW))

    def test_publication_from_last_24_hours_is_accepted(self):
        value = (self.NOW - timedelta(hours=12)).isoformat()
        self.assertTrue(is_recent_publication(value, now=self.NOW))

    def test_publication_older_than_72_hours_is_rejected(self):
        value = (self.NOW - timedelta(hours=73)).isoformat()
        self.assertFalse(is_recent_publication(value, now=self.NOW))

    def test_forwarded_message_uses_original_date(self):
        now = self.NOW

        class Header:
            date = now - timedelta(days=4)

        class Message:
            date = now - timedelta(hours=1)
            fwd_from = Header()

        publication = message_publication_datetime(Message())
        self.assertFalse(is_recent_publication(publication, now=now))

    def test_repeated_publication_has_same_message_identity_data(self):
        first = analyze_text("Ищем видеографа в Мадриде", published_at=self.NOW.isoformat())
        second = analyze_text("Ищем видеографа в Мадриде", published_at=self.NOW.isoformat())
        self.assertEqual(first["raw_text"], second["raw_text"])
        self.assertEqual(first["published_at"], second["published_at"])


if __name__ == "__main__":
    unittest.main()
