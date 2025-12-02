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

        # Send a chat completion request to gpt-4.1-mini with a system prompt to create a fuller, still concise news brief and a user prompt containing the title and original summary.
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            temperature=0.2,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You summarize news articles into compact but complete briefs. "
                        "Deliver the crux in 4-6 sentences: who/what happened, the key "
                        "drivers or context, the stakes or implications, and any next steps. "
                        "Keep facts, dates, figures, and named entities precise. Avoid fluff or speculation."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Title: {title}\n\n"
                        f"Original Summary:\n{content}\n\n"
                        "Write a single-paragraph brief that gives enough detail to understand the article without reading it."
                    ),
                },
            ],
        )

        summary_text = response.choices[0].message.content.strip()
        summarized.append({**entry, "brief_summary": summary_text})

    return summarized
