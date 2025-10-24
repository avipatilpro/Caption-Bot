import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    CAPTION_TEXT = os.getenv("CAPTION_TEXT", "")
    CAPTION_POSITION = os.getenv("CAPTION_POSITION", "bottom").lower()
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "AvishkarPatil")