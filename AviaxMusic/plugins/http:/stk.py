from pyrogram import Client, filters
from AviaxMusic import app

@app.on_message(filters.command("start"))
async def start(client, message):
    # Replace 'sticker_file_id' with the actual file ID or URL of the sticker
    sticker_file_id = "CAACAgUAAxkBAAIGJmc4uIA18pKbZrwXou93tqBwDOL-AAJaEwACIK7BVdo1lpGVyOvgNgQ"
    await message.reply_sticker(sticker_file_id)
