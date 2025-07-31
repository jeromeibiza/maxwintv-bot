from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

logging.basicConfig(level=logging.INFO)

# Liste des casinos
casinos = [
    ("FAST SLOTS 🔥 200% + 50 Free Spins +10% RB", "https://record.discasinoaffiliates.com/_au23hP5uLubk9mx2SfmU_WNd7ZgqdRLk/1/"),
    ("CASINO NIGHT 🌙 225% + 200 FS", "https://record.referaplayer.com/_nds6e0VgykJutv7iXV6HvmNd7ZgqdRLk/1/"),
    ("SHINY WILD 💎 2x125% + 25% RB", "https://partners.shinywildpartners.com/text/a8d4239f000081000023000002000002000001000001"),
    ("INSTANT CASINO 🔥 50 FS + 10€ Freebet +10% RB", "https://www.instantcasino1.com/fr?affiliateid=Hqsx1HvTucZj0CbdlJbp8mNd7ZgqdRLk"),
    ("SAMBA SLOTS 🎁 200% + 50 FS", "https://record.discasinoaffiliates.com/_au23hP5uLuZVDQsR8vgoqWNd7ZgqdRLk/1/"),
    ("GOLDEN PANDA 🐼 200% + 50 FS", "https://record.discasinoaffiliates.com/_au23hP5uLuZ8F8NfJ-N_DWNd7ZgqdRLk/1/"),
    ("BETIFY ⚽ 100% + 30 FS (code MOON)", "https://record.betify.partners/_3zudlUxeY0vqaEn2LeVpkWNd7ZgqdRLk/10/"),
    ("STAKE 🧨 30€ ou 200% (code JEROMEIBIZA)", "https://www.stake.com/?c=385f969cd2/")
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(text, url=url)] for text, url in casinos]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🎰 Clique sur un casino pour profiter du bonus :", reply_markup=reply_markup)

if __name__ == "__main__":
    import os
    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
