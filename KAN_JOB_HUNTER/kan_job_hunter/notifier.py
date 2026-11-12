import asyncio
import html
import json
import urllib.parse
import urllib.request


class Notifier:
    def __init__(self, bot_token: str, chat_id: int):
        self.bot_token, self.chat_id = bot_token, chat_id

    async def notify(self, row: dict) -> int | None:
        return await asyncio.to_thread(self._notify_sync, row)

    def _notify_sync(self, row: dict) -> int | None:
        def esc(value):
            return html.escape(str(value or "не указано"))

        text = (
            f"<b>{esc(row.get('title') or 'Новая вакансия')}</b>\n"
            f"Формат: {esc(row.get('city', 'не указан'))} / {esc(row.get('work_format', 'не указан'))}\n"
            f"Дата публикации: {esc(row.get('published_at') or 'не указана')}\n"
            f"Источник: {esc(row.get('source_title') or row.get('source_username') or 'не указан')}\n"
            f"Оплата: {esc(row.get('payment') or 'не указана')}\n"
            f"Соответствие: {float(row.get('match_score', 0)):.0%}\n\n"
            f"Почему подходит: {esc(row.get('fit_reason') or 'соответствует заданным критериям')}\n\n"
            f"{esc(row.get('description', '')[:1200])}\n\n"
            f"<a href=\"{esc(row['original_url'])}\">Оригинал объявления</a>"
        )
        markup = json.dumps({"inline_keyboard": [[
            {"text": "Открыть", "url": row["original_url"]},
            {"text": "Подготовить отклик", "callback_data": f"reply:{row['telegram_message_id']}"},
        ], [{"text": "Сохранить", "callback_data": f"save:{row['telegram_message_id']}"},
            {"text": "Неинтересно", "callback_data": f"skip:{row['telegram_message_id']}"}]]}, ensure_ascii=False)
        payload = urllib.parse.urlencode({
            "chat_id": self.chat_id, "text": text, "parse_mode": "HTML",
            "reply_markup": markup, "disable_web_page_preview": "true",
        }).encode()
        request = urllib.request.Request(
            f"https://api.telegram.org/bot{self.bot_token}/sendMessage",
            data=payload, method="POST",
        )
        with urllib.request.urlopen(request, timeout=20) as response:
            result = json.loads(response.read().decode())
        if not result.get("ok"):
            raise RuntimeError(f"Telegram Bot API error {result.get('error_code', 'unknown')}")
        result_message_id = result.get("result", {}).get("message_id")
        return int(result_message_id) if result_message_id else None
