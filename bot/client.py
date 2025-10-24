import logging
from pyrogram import Client
from bot.config import Config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class CaptionBot(Client):
    def __init__(self):
        super().__init__(
            name="CaptionBot",
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            workers=4,
            plugins=dict(root="bot.plugins")
        )