from telegram.ext import Updater, CommandHandler

from commands import start
from settings import TELEGRAM_KEY
from src.db.engine import start_db

if __name__ == '__main__':
    updater = Updater(token=TELEGRAM_KEY)
    dp = updater.dispatcher
    start_db()

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    print('Bot is polling')
    updater.idle()
