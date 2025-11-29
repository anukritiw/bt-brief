from __future__ import annotations

from html import escape
from typing import Iterable


def build_html_digest(entries: Iterable[dict], subject: str) -> str:
    items = []
    for entry in entries:
        title = escape(entry.get("title", "Untitled"))
        link = escape(entry.get("link", "#"))
        author = escape(entry.get("author", ""))
        published = entry.get("published_dt")
        published_str = published.isoformat() if published else ""
        summary = escape(entry.get("brief_summary", ""))

        items.append(
            f"""
            <article style="margin-bottom:16px;padding:12px;border:1px solid #e0e0e0;border-radius:8px;">
              <h3 style="margin:0 0 8px 0;font-family:Arial,sans-serif;">{title}</h3>
              <div style="font-size:12px;color:#555;margin-bottom:8px;">
                <span>{published_str}</span>
                {' · ' if author else ''}{author}
              </div>
              <p style="margin:0 0 8px 0;font-family:Arial,sans-serif;line-height:1.4;">{summary}</p>
              <a href="{link}" style="font-size:13px;color:#0a5bf2;text-decoration:none;">Read full article</a>
            </article>
            """
        )

    items_html = "\n".join(items) if items else "<p>No new articles in the last day.</p>"

    return f"""\
<html>
  <body style="margin:0;padding:24px;background:#f7f7f7;font-family:Arial,sans-serif;">
    <div style="max-width:720px;margin:0 auto;background:#fff;padding:24px;border-radius:12px;border:1px solid #ebebeb;">
      <h1 style="margin-top:0;font-size:22px;">{escape(subject)}</h1>
      {items_html}
    </div>
  </body>
</html>
"""
