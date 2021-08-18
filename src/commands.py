from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Hola humano'
    )
