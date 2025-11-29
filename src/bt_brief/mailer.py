from __future__ import annotations

import smtplib
import ssl
from email.message import EmailMessage

from .config import Settings

def send_digest(html_body: str, settings: Settings) -> None:
    required = [
        settings.smtp_host,
        settings.smtp_port,
        settings.smtp_user,
        settings.smtp_password,
        settings.from_email,
        settings.to_email,
    ]
    if not all(required):
        raise ValueError("SMTP configuration is incomplete. Check .env values.")

    msg = EmailMessage()
    msg["Subject"] = settings.brief_subject
    msg["From"] = settings.from_email
    msg["To"] = settings.to_email
    msg.set_content("HTML digest attached. Please use an HTML-capable email client.")
    msg.add_alternative(html_body, subtype="html")

    context = ssl.create_default_context()
    with smtplib.SMTP(settings.smtp_host, settings.smtp_port) as server:
        server.starttls(context=context)
        server.login(settings.smtp_user, settings.smtp_password)
        server.send_message(msg)

if __name__ == "__main__":
    from .config import Settings
    settings = Settings.from_env()
    send_digest("<h1>Test Digest</h1><p>This is a test email from bt-brief.</p>", settings)