from pyrogram import Client, enums, __version__
from config import Config, LOGGER 

class autocaption(Client):
    def __init__(self):
        super().__init__(
            "autocaption",
            api_hash=Config.API_HASH,
            api_id=Config.APP_ID,
            bot_token=Config.BOT_TOKEN, 
            workers=20,
            plugins={
                "root": "plugins"
            }                        
            
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        bot_details = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"@{bot_details.username}  started! "
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")



def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

app = autocaption()
app.run()
