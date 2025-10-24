import asyncio
import logging
from bot.client import CaptionBot

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

async def main():
    app = CaptionBot()
    await app.start()
    print("Bot started successfully!")
    await app.idle()

if __name__ == "__main__":
    asyncio.run(main())