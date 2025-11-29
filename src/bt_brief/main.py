from __future__ import annotations

from .config import Settings
from .digest_builder import build_html_digest
from .filter_author import filter_by_author
from .mailer import send_digest
from .rss_fetcher import fetch_recent_entries
from .summarizer import summarize_entries

def run() -> None:
    settings = Settings()

    entries = fetch_recent_entries(settings)
    filtered = filter_by_author(entries, settings.allowed_author)
    summarized = summarize_entries(filtered, settings)
    html = build_html_digest(summarized, settings.brief_subject)
    send_digest(html, settings)

if __name__ == "__main__":
    run()
