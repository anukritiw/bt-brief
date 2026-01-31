# bt-brief

Stateless daily digest builder that fetches Business Times RSS headlines, summarizes them with OpenAI, assembles an HTML digest, and emails it out via SMTP.

## Setup
- Python 3.10+
- Create/activate a virtualenv (example): `python -m venv .bt-brief-env && source .bt-brief-env/bin/activate`
- Install deps: `pip install -e .`
- Copy `.env.example` to `.env` and fill in your keys (OpenAI + SMTP). Example:

```
OPENAI_API_KEY=sk-...
RSS_URL=https://www.businesstimes.com.sg/rss/top-stories
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your.address@gmail.com
SMTP_PASSWORD=app-specific-password
FROM_EMAIL=your.address@gmail.com
TO_EMAIL=recipient@example.com
```

## Running
- Ensure your virtualenv is active (example): `source .bt-brief-env/bin/activate`
- Run `python -m bt_brief.main`
- Example daily cron hook (ensures env activation inside): `./scripts/run_daily.sh`
