import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import autocaption
from config import Config


# =
usercaption_position = Config.CAPTION_POSITION
caption_position = usercaption_position.lower()
caption_text = Config.CAPTION_TEXT


@autocaption.on_message(filters.channel & (filters.document | filters.video | filters.audio | filters.photo) & ~filters.edited, group=-1)
async def editing(bot, message):
    user_id = message.from_user.id
    user_config = user_configs.get(user_id, {})
    caption_position = user_config.get("caption_position", Config.CAPTION_POSITION).lower()
    caption_text = user_config.get("caption_text", Config.CAPTION_TEXT)

    try:
        media = message.document or message.video or message.audio or message.photo
    except Exception as e:
        logger.error(f"Error fetching media: {e}")
        return

    if (message.document or message.video or message.audio or message.photo):
        if message.caption:
            file_caption = f"**{message.caption}**"
        else:
            fname = media.file_name if hasattr(media, 'file_name') else "Media"
            filename = fname.replace("_", ".")
            file_caption = f"`{filename}`"

    try:
        if caption_position == "top":
            await bot.edit_message_caption(
                chat_id=message.chat.id,
                message_id=message.message_id,
                caption=caption_text + "\n" + file_caption,
                parse_mode="markdown"
            )
        elif caption_position == "bottom":
            await bot.edit_message_caption(
                chat_id=message.chat.id,
                message_id=message.message_id,
                caption=file_caption + "\n" + caption_text,
                parse_mode="markdown"
            )
        elif caption_position == "nil":
            await bot.edit_message_caption(
                chat_id=message.chat.id,
                message_id=message.message_id,
                caption=caption_text,
                parse_mode="markdown"
            )
    except Exception as e:
        logger.error(f"Error editing message caption: {e}")
                   
      
