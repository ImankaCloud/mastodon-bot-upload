# Mastodon-Bot-Upload
 A simple bot shares pictures from a Discord channel to a Mastodon account. use GPT-3.

# Features
Monitors a specific Discord channel for messages with image attachments
Uploads the image to Mastodon
Uses OpenAI GPT-3 to generate GTA Roleplay themed status messages for Mastodon

# 1. Clone the Repository:
```
git clone https://github.com/ImankaCloud/Mastodon-Bot-Upload.git
```

# 2. Install Dependencies:
```
pip install -r requirements.txt
```

# 3. Edit Dotenv
```
MASTODON_HOST = "https://mastodon.social"
MASTODON_TOKEN = ""
DISCORD_CHANNEL_ID = ""
OPENAI_API_KEY = ""
OPENAI_PROMPT = ""
DISCORD_BOT_TOKEN = ""
```

# 4. Run the Bot
```
python main.py
```
