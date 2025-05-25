from pyrogram import Client, filters
from pyromod import listen
from pyrogram.types import Message
import asyncio
import os

API_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH", "your_api_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")

app = Client("shortner_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):
    await message.reply_text("Hello! Send me a URL to shorten.")

@app.on_message(filters.text & filters.private)
async def url_shortener(client: Client, message: Message):
    url = message.text.strip()

    if not url.startswith("http"):
        await message.reply_text("Please send a valid URL starting with http or https.")
        return

    short_url = await shorten_url(url)
    await message.reply_text(f"Shortened URL: {short_url}")

async def shorten_url(url: str) -> str:
    # Dummy shortener logic — replace this with real API call
    return f"https://short.url/{url[-6:]}"

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
