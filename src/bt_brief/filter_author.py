from __future__ import annotations

from typing import Iterable

def filter_by_author(entries: Iterable[dict], allowed_author: str | None) -> list[dict]:
    """Return entries that match the configured author filter (if any)."""
    if not allowed_author:
        return list(entries)

    needle = allowed_author.lower()
    return [entry for entry in entries if needle in (entry.get("author", "") or "").lower()]
