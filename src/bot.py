from telegram.ext import Updater, CommandHandler

from commands import start
from settings import TELEGRAM_KEY

if __name__ == '__main__':
    updater = Updater(token=TELEGRAM_KEY)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    print('Bot is polling')
    updater.idle()
