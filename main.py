from pyrogram import Client, filters

app = Client("my_bot")

@app.on_message(filters.text)
async def handle_text(client, message):
    await message.reply("Text message received!")

app.run()
