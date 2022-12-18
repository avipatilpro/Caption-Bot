import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters, enums
from bot import autocaption
from config import Config


# =
usercaption_position = Config.CAPTION_POSITION
caption_position = usercaption_position.lower()
caption_text = Config.CAPTION_TEXT

media = filters.document | filters.video | filters.audio

@autocaption.on_message(filters.channel & media)
async def editing(bot, message):
      try:
         media = message.document or message.video or message.audio
         caption_text = Config.CAPTION_TEXT
      except:
         caption_text = ""
         pass 
      if (message.document or message.video or message.audio): 
          if message.caption:                        
             file_caption = f"**{message.caption}**"                
          else:
             fname = media.file_name
             filename = fname.replace("_", ".")
             file_caption = f"`{filename}`"  
              
      try:
          if caption_position == "top":
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.id,
                 caption = caption_text + "\n" + file_caption,
                 parse_mode = enums.ParseMode.MARKDOWN
             )
          elif caption_position == "bottom":
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.id,
                 caption = file_caption + "\n" + caption_text,
                 parse_mode = enums.ParseMode.MARKDOWN
             )
          elif caption_position == "nil":
             await bot.edit_message_caption(
                 chat_id = message.chat.id,
                 message_id = message.id,
                 caption = caption_text, 
                 parse_mode = enums.ParseMode.MARKDOWN
             ) 
      except:
          pass
              
                   
      
