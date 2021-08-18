from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters

import callbacks
import constants
import conversations
from commands import start, cancel
from settings import TELEGRAM_KEY
from db import start_db

if __name__ == '__main__':
    updater = Updater(token=TELEGRAM_KEY)
    dp = updater.dispatcher
    start_db()

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(ConversationHandler(
        entry_points=[
            CallbackQueryHandler(pattern='contact', callback=callbacks.contact_callback)
        ],
        states={
            constants.INPUT_FIRST_NAME: [MessageHandler(Filters.text, conversations.first_name_conversation)],
            constants.INPUT_LAST_NAME: [MessageHandler(Filters.text, conversations.last_name_conversation)],
            constants.INPUT_PHONE: [MessageHandler(Filters.text, conversations.phone_conversation)],
            constants.SAVE_INFO: [MessageHandler(Filters.text, conversations.save_info_conversation)],
        },
        fallbacks=[
            CommandHandler('cancel', cancel)
        ]
    ))

    updater.start_polling()
    print('Bot is polling')
    updater.idle()
