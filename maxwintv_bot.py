
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8355178835:AAH460fjfgwYbGBM5FEtzzhtUhTk6EM6dBA"

casinos = [
    ("FAST SLOTS 🔥", "Bonus 200% + 50 tours gratuits +10% de rakeback", "https://record.discasinoaffiliates.com/_au23hP5uLubk9mx2SfmU_WNd7ZgqdRLk/1/"),
    ("CASINO NIGHT 🌙", "225% + 200 Tours Gratuits", "https://record.referaplayer.com/_nds6e0VgykJutv7iXV6HvmNd7ZgqdRLk/1/"),
    ("SHINY WILD 💎", "2x125% + 25% rakeback", "https://partners.shinywildpartners.com/text/a8d4239f000081000023000002000002000001000001"),
    ("INSTANT CASINO 🔥", "50 Tours gratuits + 10€ freebet +10% de rakeback", "https://www.instantcasino1.com/fr?affiliateid=Hqsx1HvTucZj0CbdlJbp8mNd7ZgqdRLk"),
    ("SAMBA SLOTS 🎁", "200% + 50 Tours Gratuits", "https://record.discasinoaffiliates.com/_au23hP5uLuZVDQsR8vgoqWNd7ZgqdRLk/1/"),
    ("GOLDEN PANDA 🐼", "200% + 50 Tours gratuits", "https://record.discasinoaffiliates.com/_au23hP5uLuZ8F8NfJ-N_DWNd7ZgqdRLk/1/"),
    ("BETIFY ⚽", "100% + 30 Tours gratuits avec le code MOON", "https://record.betify.partners/_3zudlUxeY0vqaEn2LeVpkWNd7ZgqdRLk/10/"),
    ("STAKE 🧨", "30€ offerts ou 200% avec le code JEROMEIBIZA", "https://www.stake.com/?c=385f969cd2/")
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = "👋 Bienvenue sur MaxWinTV ! Voici nos casinos partenaires :"
    await update.message.reply_text(welcome_text)

    for casino in casinos:
        name, bonus, url = casino
        text = f"🎰 {name}\n{bonus}"
        button = [[InlineKeyboardButton("🎁 Profiter du bonus", url=url)]]
        reply_markup = InlineKeyboardMarkup(button)
        await update.message.reply_text(text, reply_markup=reply_markup)

def main():
    logging.basicConfig(level=logging.INFO)
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
