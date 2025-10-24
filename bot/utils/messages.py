class Messages:
    START_TEXT = """
👋 **Hello** {}!

I'm an **Auto Caption Bot** that automatically adds custom captions to media files in your channels.

**Features:**
• Supports all media types (photos, videos, documents, audio)
• Customizable caption text with markdown support
• Flexible positioning (top, bottom, or replace)
• Works in both public and private channels

Maintained by @{}
"""

    HELP_TEXT = """
<b>📖 How to Use</b>

<b>Setup Steps:</b>
1. Add me as admin in your channel with edit message permissions
2. Set your custom caption text in environment variables
3. Upload or forward media files to your channel
4. I'll automatically edit the captions!

<b>Caption Formatting:</b>
Supports full markdown formatting including bold, italic, code, and links.

<b>Source Code:</b> https://github.com/avipatilpro/Caption-Bot
"""

    ABOUT_TEXT = """
<b>ℹ️ About This Bot</b>

<b>Bot Name:</b> Auto Caption Bot
<b>Language:</b> Python
<b>Framework:</b> Pyrofork
<b>Version:</b> 3.0.0
<b>Features:</b> Auto caption, Markdown support, Multi-position

Built with ❤️ for the Telegram community
"""

    MARKDOWN_TEXT = """
<b>📝 Markdown Guide</b>

<b>Bold Text:</b>
<code>**Your Text**</code>

<b>Italic Text:</b>
<code>__Your Text__</code>

<b>Code Text:</b>
<code>`Your Code`</code>

<b>Links:</b>
<code>[Link Text](https://example.com)</code>

<b>Combined:</b>
<code>**Bold** and __italic__ with `code`</code>
"""

    STATUS_TEXT = """
<b>⚙️ Current Settings</b>

<b>Caption Text:</b>
<code>{}</code>

<b>Position:</b> <code>{}</code>

<i>You can modify these settings through environment variables.</i>
"""