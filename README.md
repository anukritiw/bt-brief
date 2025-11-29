# bt-brief

Stateless daily digest builder that fetches Business Times RSS headlines, summarizes them with OpenAI, assembles an HTML digest, and emails it out via SMTP.

## Setup
- Python 3.10+
- `pip install -e .`
- Copy `.env.example` to `.env` and fill in your keys.

## Running
- From the repo root (after installing dependencies): `python -m bt_brief.main`
- As requested, you can also invoke via: `python -m bt-brief.main`
- Example daily cron hook: `./scripts/run_daily.sh`
