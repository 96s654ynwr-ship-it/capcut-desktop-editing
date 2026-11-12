from __future__ import annotations

import re
from datetime import date, datetime, timezone


PROFESSION_TERMS = {
    "photographer": ["фотограф", "фотосъем", "фотосъём", "photo", "fotógrafo", "fotografo", "fotografía", "fotografia"],
    "videographer": ["видеограф", "videographer", "съемка видео", "съёмка видео", "videógrafo", "videografo"],
    "camera_operator": ["оператор", "кинооператор", "camera operator", "видеосъемка", "видеосъёмка", "operador de cámara", "operador de camara"],
    "video_editor": ["видеомонтаж", "монтажер", "монтажёр", "монтаж видео", "editor", "premiere pro", "davinci", "editor de video", "edición de video", "edicion de video", "montaje de video"],
    "video_teacher": ["преподаватель видеосъемки", "преподаватель видеосъёмки", "курс видеосъемки", "курс видеосъёмки", "profesor de vídeo", "profesor de video", "curso de vídeo", "curso de video"],
    "editing_teacher": ["преподаватель монтажа", "обучение монтажу", "цветокоррекции", "цветокоррекция", "curso de edición", "curso de edicion", "formación audiovisual"],
}
EXCLUDED_TERMS = ["ai-креатор", "ai creator", "нейросет", "генеративн", "motion designer", "моушн-дизайн", "моушн дизайнер"]
MADRID = ["мадрид", "madrid"]
BARCELONA = ["барселон", "barcelona", "bcn"]
REMOTE = ["удален", "удалён", "remote", "дистанцион", "из любой точки", "relocation not required"]
RUSSIAN = ["русск", "russian", "на русском", "на русском языке"]
PAYMENT_RE = re.compile(r"(?:€|eur|руб(?:лей|\.| )?|₽|usd|\$)\s?\d[\d\s.,]*|\d[\d\s.,]*\s?(?:€|eur|руб(?:лей|\.| )?|₽|usd|\$)", re.I)


def _contains(text: str, terms: list[str]) -> bool:
    return any(term in text for term in terms)


def message_publication_datetime(message) -> datetime | None:
    """Return the original Telegram publication time in UTC when available."""
    forwarded = getattr(message, "fwd_from", None)
    value = getattr(forwarded, "date", None) or getattr(message, "date", None)
    if value is None:
        return None
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def parse_publication_datetime(value: str | datetime | None) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        parsed = value
    else:
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except (TypeError, ValueError):
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def publication_age_hours(value: str | datetime | None, *, now: datetime | None = None) -> float | None:
    parsed = parse_publication_datetime(value)
    if parsed is None:
        return None
    current = now or datetime.now(timezone.utc)
    if current.tzinfo is None:
        current = current.replace(tzinfo=timezone.utc)
    return round((current.astimezone(timezone.utc) - parsed).total_seconds() / 3600, 3)


def is_recent_publication(
    value: str | datetime | None,
    *,
    now: datetime | None = None,
    max_age_hours: int = 72,
) -> bool:
    age = publication_age_hours(value, now=now)
    return age is not None and 0 <= age <= max_age_hours


def current_city(today: date | None = None) -> str:
    today = today or date.today()
    return "Барселона" if today >= date(2026, 12, 1) else "Мадрид"


def analyze_text(text: str, *, published_at: str | None = None) -> dict:
    raw = text.strip()
    normalized = raw.lower()
    professions = [key for key, terms in PROFESSION_TERMS.items() if _contains(normalized, terms)]
    excluded = _contains(normalized, EXCLUDED_TERMS)
    remote = _contains(normalized, REMOTE)
    city = ""
    if _contains(normalized, MADRID): city = "Мадрид"
    elif _contains(normalized, BARCELONA): city = "Барселона"
    language = "русский" if _contains(normalized, RUSSIAN) else "не указан"
    score = 0.0
    score += min(len(professions), 2) * 0.28
    score += 0.20 if remote else 0.0
    score += 0.20 if city == current_city() else 0.0
    score += 0.12 if language == "русский" else 0.0
    score += 0.10 if PAYMENT_RE.search(raw) else 0.0
    if excluded: score -= 0.8
    relevant = bool(professions) and not excluded and score >= 0.28
    title = next((line.strip(" -*•#") for line in raw.splitlines() if line.strip()), "Вакансия без заголовка")[:160]
    contact = None
    match = re.search(r"(?:@|t\.me/)[\w_]{4,}", raw, re.I)
    if match: contact = match.group(0)
    reasons = list(professions)
    if city: reasons.append(city)
    if remote: reasons.append("удалённый формат")
    if language == "русский": reasons.append("русский язык")
    return {
        "relevant": relevant,
        "professions": professions,
        "work_format": "remote" if remote else ("onsite" if city else "not_specified"),
        "city": city or "не указан",
        "language": language,
        "payment": PAYMENT_RE.search(raw).group(0) if PAYMENT_RE.search(raw) else None,
        "contact": contact,
        "fit_reason": ", ".join(reasons),
        "title": title,
        "description": raw[:1200],
        "match_score": round(max(0.0, min(1.0, score)), 3),
        "published_at": published_at,
        "publication_age_hours": publication_age_hours(published_at),
        "raw_text": raw,
    }


def discovery_queries() -> list[str]:
    return [
        "видеограф Мадрид", "видеомонтаж Мадрид", "фотограф Мадрид", "оператор Мадрид",
        "videographer Madrid", "fotógrafo Madrid", "producción audiovisual Madrid", "editor de video Madrid",
        "Premiere Pro Madrid", "DaVinci Resolve Madrid", "видеограф Барселона", "видеомонтаж Барселона",
        "фотограф Барселона", "оператор Барселона", "videographer Barcelona", "fotógrafo Barcelona",
        "producción audiovisual Barcelona", "editor de video Barcelona", "Premiere Pro Barcelona",
        "съемка видео удаленно русский", "видеомонтаж удаленно русский", "оператор удаленная работа русский",
        "видеограф удаленно русский", "монтаж Premiere удаленно", "монтаж DaVinci удаленно",
        "преподаватель видеомонтажа", "курс видеосъемки", "курс цветокоррекции", "video editing jobs russian",
    ]
