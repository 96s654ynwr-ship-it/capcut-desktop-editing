from __future__ import annotations

import re
from datetime import date


PROFESSION_TERMS = {
    "photographer": ["фотограф", "фотосъем", "фотосъём", "photo"],
    "videographer": ["видеограф", "videographer", "съемка видео", "съёмка видео"],
    "camera_operator": ["оператор", "кинооператор", "camera operator", "видеосъемка", "видеосъёмка"],
    "video_editor": ["видеомонтаж", "монтажер", "монтажёр", "монтаж видео", "editor", "premiere pro", "davinci"],
    "video_teacher": ["преподаватель видеосъемки", "преподаватель видеосъёмки", "курс видеосъемки", "курс видеосъёмки"],
    "editing_teacher": ["преподаватель монтажа", "обучение монтажу", "цветокоррекции", "цветокоррекция"],
}
EXCLUDED_TERMS = ["ai-креатор", "ai creator", "нейросет", "генеративн", "motion designer", "моушн-дизайн", "моушн дизайнер"]
MADRID = ["мадрид", "madrid"]
BARCELONA = ["барселон", "barcelona", "bcn"]
REMOTE = ["удален", "удалён", "remote", "дистанцион", "из любой точки", "relocation not required"]
RUSSIAN = ["русск", "russian", "на русском", "на русском языке"]
PAYMENT_RE = re.compile(r"(?:€|eur|руб(?:лей|\.| )?|₽|usd|\$)\s?\d[\d\s.,]*|\d[\d\s.,]*\s?(?:€|eur|руб(?:лей|\.| )?|₽|usd|\$)", re.I)


def _contains(text: str, terms: list[str]) -> bool:
    return any(term in text for term in terms)


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
    return {
        "relevant": relevant,
        "professions": professions,
        "work_format": "remote" if remote else ("onsite" if city else "not_specified"),
        "city": city or "не указан",
        "language": language,
        "payment": PAYMENT_RE.search(raw).group(0) if PAYMENT_RE.search(raw) else None,
        "contact": contact,
        "title": title,
        "description": raw[:1200],
        "match_score": round(max(0.0, min(1.0, score)), 3),
        "published_at": published_at,
        "raw_text": raw,
    }


def discovery_queries() -> list[str]:
    return [
        "видеограф Мадрид", "видеомонтаж Мадрид", "фотограф Мадрид",
        "оператор Мадрид", "съемка видео удаленно русский",
        "видеограф Барселона", "видеомонтаж Барселона", "фотограф Барселона",
        "оператор удаленная работа русский", "преподаватель видеомонтажа",
    ]
