FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN groupadd --system app && useradd --system --gid app --home-dir /app app

COPY requirements.txt pyproject.toml ./
RUN pip install --no-cache-dir -r requirements.txt

COPY kan_job_hunter ./kan_job_hunter
COPY start.sh README.md ./
RUN chmod +x start.sh && mkdir -p /app/data /app/logs && chown -R app:app /app

USER app

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD python -m kan_job_hunter health || exit 1

CMD ["python", "-m", "kan_job_hunter", "run"]
