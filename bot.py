import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

CASINOS = [
    ("🔥 Fast Slots", "https://record.discasinoaffiliates.com/_au23hP5uLubk9mx2SfmU_WNd7ZgqdRLk/1/"),
    ("🌙 Casino Night", "https://record.referaplayer.com/_nds6e0VgykJutv7iXV6HvmNd7ZgqdRLk/1/"),
    ("💎 Shiny Wild", "https://partners.shinywildpartners.com/text/a8d4239f000081000023000002000002000001000001"),
    ("🔥 Instant Casino", "https://www.instantcasino1.com/fr?affiliateid=Hqsx1HvTucZj0CbdlJbp8mNd7ZgqdRLk"),
    ("🎁 Samba Slots", "https://record.discasinoaffiliates.com/_au23hP5uLuZVDQsR8vgoqWNd7ZgqdRLk/1/"),
    ("🐼 Golden Panda", "https://record.discasinoaffiliates.com/_au23hP5uLuZ8F8NfJ-N_DWNd7ZgqdRLk/1/"),
    ("⚽ Betify", "https://record.betify.partners/_3zudlUxeY0vqaEn2LeVpkWNd7ZgqdRLk/10/"),
    ("🧨 Stake", "https://www.stake.com/?c=385f969cd2/")
]

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    buttons = [types.InlineKeyboardButton(text=name, url=url) for name, url in CASINOS]
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(*buttons)
    await message.answer("🎰 Bienvenue sur Maxwintv Bot !
Choisis ton casino ci-dessous :", reply_markup=kb)

@dp.message_handler(commands=["bonus"])
async def bonus(message: types.Message):
    text = "<b>🎁 Bonus disponibles :</b>

"
    for name, url in CASINOS:
        text += f"{name} ➡️ <a href='{url}'>CLAIM</a>
"
    await message.answer(text)

@dp.message_handler(commands=["support"])
async def support(message: types.Message):
    await message.answer("📩 Pour toute question, contacte-nous ici :
@jeromeibizalive")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
