"""Local-only Telegram QR authorization.

The QR payload and session are never printed or committed. The QR image is
written to ignored data/ and opened locally for scanning from an iPhone.
"""

from __future__ import annotations

import asyncio
import getpass
import logging
import subprocess
from pathlib import Path

import qrcode
from telethon import TelegramClient, errors

from .config import get_settings


logger = logging.getLogger(__name__)


def write_qr(url: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    image = qrcode.make(url)
    image.save(path)


def open_locally(path: Path) -> None:
    try:
        subprocess.run(["open", str(path)], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except OSError:
        pass


async def main() -> None:
    settings = get_settings()
    settings.validate_user()
    qr_path = settings.resolve("data/telegram_login_qr.png")
    client = TelegramClient(str(settings.session_path), settings.telegram_api_id, settings.telegram_api_hash)
    try:
        await client.connect()
        if await client.is_user_authorized():
            me = await client.get_me()
            print(f"Already authorized: {'yes' if me else 'unknown'}")
            return
        while True:
            login = await client.qr_login()
            write_qr(login.url, qr_path)
            open_locally(qr_path)
            print("QR code opened locally. Scan it in Telegram: Settings → Devices → Link Desktop Device.")
            print(f"QR image path: {qr_path}")
            try:
                await login.wait()
                break
            except asyncio.TimeoutError:
                print("QR expired; generating a new local QR code.")
                continue
            except errors.SessionPasswordNeededError:
                password = getpass.getpass("Telegram 2FA password (local terminal only): ")
                await client.sign_in(password=password)
                break
        me = await client.get_me()
        print(f"QR authorization successful: {'yes' if me else 'no'}")
    finally:
        try:
            qr_path.unlink(missing_ok=True)
        except OSError:
            pass
        await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
