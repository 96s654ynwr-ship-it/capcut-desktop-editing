import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


SCHEMA = """
CREATE TABLE IF NOT EXISTS sources (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  telegram_id INTEGER NOT NULL UNIQUE,
  username TEXT UNIQUE,
  title TEXT NOT NULL,
  source_type TEXT NOT NULL,
  relevance_score REAL NOT NULL,
  languages_json TEXT NOT NULL,
  joined INTEGER NOT NULL DEFAULT 0,
  enabled INTEGER NOT NULL DEFAULT 1,
  last_checked_at TEXT,
  last_message_id INTEGER,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS messages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  source_id INTEGER NOT NULL REFERENCES sources(id),
  telegram_message_id INTEGER NOT NULL,
  published_at TEXT,
  title TEXT,
  work_format TEXT,
  city TEXT,
  payment TEXT,
  language TEXT,
  contact TEXT,
  description TEXT NOT NULL,
  match_score REAL NOT NULL,
  original_url TEXT,
  raw_text TEXT NOT NULL,
  notified_at TEXT,
  status TEXT NOT NULL DEFAULT 'new',
  UNIQUE(source_id, telegram_message_id)
);
CREATE TABLE IF NOT EXISTS search_runs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  run_type TEXT NOT NULL,
  query TEXT,
  status TEXT NOT NULL,
  found_count INTEGER NOT NULL DEFAULT 0,
  error TEXT,
  started_at TEXT NOT NULL,
  finished_at TEXT
);
CREATE TABLE IF NOT EXISTS action_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  action TEXT NOT NULL,
  message_id INTEGER,
  payload_json TEXT,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS notification_attempts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  message_id INTEGER NOT NULL UNIQUE REFERENCES messages(id),
  status TEXT NOT NULL,
  attempt_count INTEGER NOT NULL DEFAULT 0,
  provider_message_id INTEGER,
  last_error TEXT,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);
"""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class Database:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("PRAGMA journal_mode = WAL")
        return connection

    def initialize(self) -> None:
        with self.connect() as connection:
            connection.executescript(SCHEMA)

    def upsert_source(self, row: dict) -> int:
        now = utc_now()
        with self.connect() as c:
            c.execute("""INSERT INTO sources
              (telegram_id, username, title, source_type, relevance_score, languages_json, created_at, updated_at)
              VALUES (?, ?, ?, ?, ?, ?, ?, ?)
              ON CONFLICT(telegram_id) DO UPDATE SET username=excluded.username,title=excluded.title,
              source_type=excluded.source_type,relevance_score=excluded.relevance_score,
              languages_json=excluded.languages_json,updated_at=excluded.updated_at""",
                (row["telegram_id"], row.get("username"), row["title"], row["source_type"],
                 row["relevance_score"], json.dumps(row.get("languages", []), ensure_ascii=False), now, now))
            return int(c.execute("SELECT id FROM sources WHERE telegram_id=?", (row["telegram_id"],)).fetchone()[0])

    def upsert_message(self, source_id: int, row: dict) -> int:
        with self.connect() as c:
            c.execute("""INSERT OR IGNORE INTO messages
              (source_id, telegram_message_id, published_at, title, work_format, city, payment,
               language, contact, description, match_score, original_url, raw_text)
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (source_id, row["telegram_message_id"], row.get("published_at"), row.get("title"),
                 row.get("work_format"), row.get("city"), row.get("payment"), row.get("language"),
                 row.get("contact"), row["description"], row["match_score"], row.get("original_url"), row["raw_text"]))
            return int(c.execute("SELECT id FROM messages WHERE source_id=? AND telegram_message_id=?",
                                 (source_id, row["telegram_message_id"])).fetchone()[0])

    def claim_notification(self, message_id: int) -> bool:
        now = utc_now()
        with self.connect() as c:
            if c.execute("SELECT notified_at FROM messages WHERE id=?", (message_id,)).fetchone()[0] is not None:
                return False
            c.execute("""INSERT INTO notification_attempts
              (message_id,status,attempt_count,created_at,updated_at) VALUES(?,?,?,?,?)
              ON CONFLICT(message_id) DO UPDATE SET status='in_progress',
              attempt_count=notification_attempts.attempt_count+1,updated_at=excluded.updated_at""",
                      (message_id, "in_progress", 1, now, now))
            return True

    def mark_notification_sent(self, message_id: int, provider_message_id: int | None = None) -> None:
        now = utc_now()
        with self.connect() as c:
            c.execute("UPDATE messages SET notified_at=? WHERE id=?", (now, message_id))
            c.execute("UPDATE notification_attempts SET status='sent',provider_message_id=?,updated_at=? WHERE message_id=?",
                      (provider_message_id, now, message_id))

    def mark_notification_failed(self, message_id: int, error: str) -> None:
        with self.connect() as c:
            c.execute("UPDATE notification_attempts SET status='failed',last_error=?,updated_at=? WHERE message_id=?",
                      (error[:500], utc_now(), message_id))

    def mark_checked(self, telegram_id: int, message_id: int | None) -> None:
        with self.connect() as c:
            c.execute("UPDATE sources SET last_checked_at=?, last_message_id=?, updated_at=? WHERE telegram_id=?",
                      (utc_now(), message_id, utc_now(), telegram_id))

    def log_action(self, action: str, message_id: int | None = None, payload: dict | None = None) -> None:
        with self.connect() as c:
            c.execute("INSERT INTO action_log(action,message_id,payload_json,created_at) VALUES(?,?,?,?)",
                      (action, message_id, json.dumps(payload or {}, ensure_ascii=False), utc_now()))

    def mark_notified(self, message_db_id: int) -> None:
        with self.connect() as c:
            c.execute("UPDATE messages SET notified_at=? WHERE id=?", (utc_now(), message_db_id))
