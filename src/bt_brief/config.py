from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    rss_url: str = os.getenv("RSS_URL", "https://www.businesstimes.com.sg/rss/top-stories")
    allowed_author: str | None = os.getenv("ALLOWED_AUTHOR") or None
    lookback_hours: int = int(os.getenv("LOOKBACK_HOURS", "24")) # frequency of brief
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")        # for summarization
    smtp_host: str = os.getenv("SMTP_HOST", "smtp.gmail.com")    # Gmail SMTP
    smtp_port: int = int(os.getenv("SMTP_PORT", "587"))          # Gmail SMTP port
    smtp_user: str = os.getenv("SMTP_USER", "")                  # email
    smtp_password: str = os.getenv("SMTP_PASSWORD", "")          # app password  
    from_email: str = os.getenv("FROM_EMAIL", "")                # sender email
    to_email: str = os.getenv("TO_EMAIL", "")                    # recipient email
    brief_subject: str = os.getenv("BRIEF_SUBJECT", "Business Times Daily Brief") # email subject
