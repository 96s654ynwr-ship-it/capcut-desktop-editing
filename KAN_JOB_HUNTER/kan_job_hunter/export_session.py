"""Export a local Telethon file session to an ignored StringSession file.

The session string is never printed. The output file must be copied manually
to a GitHub Actions Secret by the user, then securely deleted locally if desired.
"""

import asyncio
import os
from pathlib import Path

from telethon import TelegramClient
from telethon.sessions import StringSession

from .config import get_settings


async def main() -> None:
    settings = get_settings()
    settings.validate_user()
    output = settings.resolve("data/telegram_session_string.txt")
    client = TelegramClient(str(settings.session_path), settings.telegram_api_id, settings.telegram_api_hash)
    try:
        await client.connect()
        if not await client.is_user_authorized():
            raise RuntimeError("Local user session is not authorized")
        session_string = StringSession.save(client.session)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(session_string + "\n", encoding="utf-8")
        os.chmod(output, 0o600)
        print(f"StringSession exported to ignored local file: {output}")
    finally:
        await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
