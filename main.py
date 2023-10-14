import discord
import requests
import openai
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Mastodon API endpoint and token
mastodon_host = os.getenv("MASTODON_HOST")
token = os.getenv("MASTODON_TOKEN")
bot_token = os.getenv("DISCORD_BOT_TOKEN")
prompt_ai = os.getenv("OPENAI_PROMPT")

headers = {
    'Authorization': f'Bearer {token}'
}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    print("Received a message")
    if message.channel.id == int(os.getenv("DISCORD_CHANNEL_ID")):
        print("Message is in the correct channel")
        if message.attachments:
            print("Message has attachments")
            for attachment in message.attachments:
                img_url = attachment.url
                img_data = requests.get(img_url).content
                files = {'file': img_data}

                # Upload image to Mastodon
                response = requests.post(f"{mastodon_host}/api/v2/media", headers=headers, files=files)
                print(f"Mastodon Response: {response.status_code}")
                
                if response.status_code == 200 or response.status_code == 202:
                    uploaded_media = response.json()
                    media_id = uploaded_media["id"]
                    
                    # Generate GTA Roleplay themed status using GPT-3 API
                    openai.api_key = os.getenv("OPENAI_API_KEY")
                    gpt3_response = openai.Completion.create(
                        engine="text-davinci-002",  
                        prompt=prompt_ai,
                        max_tokens=50  
                    )
                    generated_status = gpt3_response.choices[0].text.strip()
                    print(generated_status)
                    
                    data = {
                        'status': generated_status,
                        'media_ids[]': media_id
                    }
                    mastodon_response = requests.post(f"{mastodon_host}/api/v1/statuses", headers=headers, data=data)
                    print(f"Mastodon Status Post Response: {mastodon_response.status_code}")

bot.run(bot_token)