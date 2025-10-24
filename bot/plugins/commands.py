from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot.client import CaptionBot
from bot.config import Config
from bot.utils.messages import Messages

app = CaptionBot()

@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    await message.reply_text(
        Messages.START_TEXT.format(message.from_user.first_name, Config.ADMIN_USERNAME),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🖋 Current Caption", callback_data="status")],
            [
                InlineKeyboardButton("🤩 Help", callback_data="help"),
                InlineKeyboardButton("🛡 About", callback_data="about")
            ],
            [InlineKeyboardButton("🔐 Close", callback_data="close")]
        ]),
        parse_mode="markdown",
        disable_web_page_preview=True
    )

@app.on_message(filters.command("help") & filters.private)
async def help_command(client, message):
    await message.reply_text(
        Messages.HELP_TEXT,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("About Markdown", callback_data="markdown")],
            [
                InlineKeyboardButton("⏪ Back", callback_data="back"),
                InlineKeyboardButton("🔐 Close", callback_data="close")
            ]
        ]),
        parse_mode="html",
        disable_web_page_preview=True
    )

@app.on_message(filters.command("about") & filters.private)
async def about_command(client, message):
    await message.reply_text(
        Messages.ABOUT_TEXT,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("⬇️ Back", callback_data="back"),
                InlineKeyboardButton("🔐 Close", callback_data="close")
            ],
            [InlineKeyboardButton("🤩 Help", callback_data="help")]
        ]),
        parse_mode="markdown",
        disable_web_page_preview=True
    )

@app.on_callback_query()
async def callback_handler(client, callback_query: CallbackQuery):
    data = callback_query.data
    
    if data == "status":
        await callback_query.message.edit_text(
            Messages.STATUS_TEXT.format(Config.CAPTION_TEXT, Config.CAPTION_POSITION),
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("⬇️ Back", callback_data="back"),
                    InlineKeyboardButton("🔐 Close", callback_data="close")
                ]
            ]),
            parse_mode="html"
        )
    
    elif data == "help":
        await callback_query.message.edit_text(
            Messages.HELP_TEXT,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("About Markdown", callback_data="markdown")],
                [
                    InlineKeyboardButton("⬇️ Back", callback_data="back"),
                    InlineKeyboardButton("🔐 Close", callback_data="close")
                ]
            ]),
            parse_mode="html"
        )
    
    elif data == "about":
        await callback_query.message.edit_text(
            Messages.ABOUT_TEXT,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("⬇️ Back", callback_data="back"),
                    InlineKeyboardButton("🔐 Close", callback_data="close")
                ],
                [InlineKeyboardButton("🤩 Help", callback_data="help")]
            ]),
            parse_mode="markdown"
        )
    
    elif data == "markdown":
        await callback_query.message.edit_text(
            Messages.MARKDOWN_TEXT,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("⬇️ Back", callback_data="help"),
                    InlineKeyboardButton("🔐 Close", callback_data="close")
                ]
            ]),
            parse_mode="html"
        )
    
    elif data == "back":
        await callback_query.message.edit_text(
            Messages.START_TEXT.format(callback_query.from_user.first_name, Config.ADMIN_USERNAME),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🖋 Current Caption", callback_data="status")],
                [
                    InlineKeyboardButton("🤩 Help", callback_data="help"),
                    InlineKeyboardButton("🛡 About", callback_data="about")
                ],
                [InlineKeyboardButton("🔐 Close", callback_data="close")]
            ]),
            parse_mode="markdown"
        )
    
    elif data == "close":
        await callback_query.message.delete()
        if callback_query.message.reply_to_message:
            await callback_query.message.reply_to_message.delete()