<h1 align='center'>🖊️ TG AutoCaption Bot </h1>

<h4 align='center'>Telegram Auto Caption Bot With Custom Text & Better Structure<br><br><i>(Works in channels - public or private)</i> </h4><br>

[//]: # (<h4 align='center'>✯ Demo Bot ✯<br></h4>)

[//]: # (<h3 align='center' ><b><a href="https://telegram.me/CapXBot">¢αρтισи вσт</a></b></h3>)

### ✨ Features

- Auto caption for all media files in channels
- Customizable caption text with markdown support
- Flexible caption positioning (Top/Bottom/Replace)
- Clean and organized code structure
- Updated to latest Pyrofork
- Environment variable support
- Easy deployment options

### 📋 Config Variables

- `BOT_TOKEN` - Your Bot Token from [@BotFather](https://t.me/BotFather)
- `API_ID` - Your API ID from [my.telegram.org](https://my.telegram.org)
- `API_HASH` - Your API Hash from [my.telegram.org](https://my.telegram.org)
- `CAPTION_TEXT` - Your Custom Caption Text [Supports Markdown]
- `CAPTION_POSITION` - Caption Position: `top`, `bottom`, or `nil` (replace)
- `ADMIN_USERNAME` - Your Username (without @)

### 🚀 Deploy

#### Heroku Deploy
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

#### Manual Deploy

1. **Clone Repository**
   ```bash
   git clone https://github.com/avipatilpro/Caption-Bot
   cd Caption-Bot
   ```

2. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env with your values
   ```

4. **Run Bot**
   ```bash
   python main.py
   ```

#### Docker Deploy

```bash
# Clone repository
git clone https://github.com/avipatilpro/Caption-Bot
cd Caption-Bot

# Set environment variables in .env file
cp .env.example .env
# Edit .env with your values

# Run with Docker Compose
docker-compose up -d
```

### 🤖 Commands

```
/start - Start the bot
/help  - Get help information
/about - About the bot
```



### 🔧 Setup Instructions

1. Create a bot via [@BotFather](https://t.me/BotFather)
2. Get API credentials from [my.telegram.org](https://my.telegram.org)
3. Add bot as admin in your channel with edit permissions
4. Deploy using any method above
5. Set your custom caption and position

---

**[© Avishkar Patil](https://github.com/avipatilpro)**
