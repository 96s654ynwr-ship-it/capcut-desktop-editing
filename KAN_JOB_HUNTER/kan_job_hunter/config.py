from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


ROOT_DIR = Path(__file__).resolve().parents[1]


class Settings(BaseSettings):
    telegram_api_id: int | None = None
    telegram_api_hash: str | None = None
    telegram_session_path: str = "data/job_hunter_user"
    telegram_session_string: str | None = None
    state_repo: str | None = None
    state_repo_token: str | None = None
    bot_token: str | None = None
    notification_chat_id: int | None = None
    bot_session_path: str = "data/job_hunter_bot"
    database_path: str = "data/kan_job_hunter.sqlite3"
    log_dir: str = "logs"
    poll_interval_seconds: int = 300
    discovery_interval_seconds: int = 3600
    discovery_limit_per_query: int = 20
    recent_messages_per_source: int = 30
    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_file=ROOT_DIR / ".env", extra="ignore")

    def resolve(self, value: str) -> Path:
        path = Path(value).expanduser()
        return path if path.is_absolute() else ROOT_DIR / path

    @property
    def session_path(self) -> Path:
        return self.resolve(self.telegram_session_path)

    @property
    def bot_session(self) -> Path:
        return self.resolve(self.bot_session_path)

    @property
    def db_path(self) -> Path:
        return self.resolve(self.database_path)

    @property
    def logs_path(self) -> Path:
        return self.resolve(self.log_dir)

    def validate_user(self) -> None:
        if not self.telegram_api_id or not self.telegram_api_hash:
            raise RuntimeError("Заполните TELEGRAM_API_ID и TELEGRAM_API_HASH в локальном .env")

    def validate_bot(self) -> None:
        if not self.bot_token or self.notification_chat_id is None:
            raise RuntimeError("Для уведомлений заполните BOT_TOKEN и NOTIFICATION_CHAT_ID в локальном .env")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
