from __future__ import annotations

from datetime import datetime, timedelta, timezone
import time
import feedparser

from .config import Settings

def fetch_recent_entries(settings: Settings) -> list[dict]:
    """Fetch RSS entries within the configured lookback window."""
    # parse the RSS feed
    feed = feedparser.parse(settings.rss_url)
    # determine the cutoff datetime
    cutoff = datetime.now(timezone.utc) - timedelta(hours=settings.lookback_hours)
    recent: list[dict] = []

    for entry in feed.entries:
        published_struct = entry.get("published_parsed") or entry.get("updated_parsed")
        # skip entries without a valid published date
        if not published_struct:
            continue

        # convert to datetime in UTC
        published_dt = datetime.fromtimestamp(time.mktime(published_struct), tz=timezone.utc)
        # keep entries published on or after cutoff
        if published_dt >= cutoff:
            entry["published_dt"] = published_dt
            recent.append(entry)

    # sort entries by published date descending so newest first
    recent.sort(key=lambda e: e["published_dt"], reverse=True)
    return recent
