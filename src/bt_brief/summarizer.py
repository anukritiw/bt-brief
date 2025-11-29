from __future__ import annotations

from openai import OpenAI

from .config import Settings

def summarize_entries(entries: list[dict], settings: Settings) -> list[dict]:
    if not entries:
        return []

    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY is required for summarization.")

    client = OpenAI(api_key=settings.openai_api_key)
    summarized: list[dict] = []

    # For each entry, grab the entry’s summary or description (fallback empty) and title (default “Untitled”).
    for entry in entries:
        content = entry.get("summary") or entry.get("description") or ""
        title = entry.get("title", "Untitled")

        # Send a chat completion request to gpt-4.1-mini with a system prompt to create a concise 2–3 sentence news brief and a user prompt containing the title and original summary.
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            temperature=0.2,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You condense news articles into crisp 2-3 sentence briefs. "
                        "Keep the key facts, dates, and impact. Avoid speculation."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Title: {title}\n\n"
                        f"Original Summary:\n{content}\n\n"
                        "Write a concise digest version."
                    ),
                },
            ],
        )

        summary_text = response.choices[0].message.content.strip()
        summarized.append({**entry, "brief_summary": summary_text})

    return summarized
