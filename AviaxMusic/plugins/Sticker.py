from pyrogram import Client, filters
from AviaxMusic import app

@app.on_message(filters.command("start"))
async def start(client, message):
    # Replace 'sticker_file_id' with the actual file ID or URL of the sticker
    sticker_file_id = "CAACAgUAAxkBAAJE8GK4EsoLVZC2SW5W5Q-QAkaoN8f_AAL9BQACiy14VGoQxOCDfE1KKQQ"
    await message.reply_sticker(sticker_file_id)
