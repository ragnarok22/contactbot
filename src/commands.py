from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Hola humano'
    )


def cancel(update, context):
    update.message.reply_text(
        text='La acción ha sido cancelada',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Contactar con humano', callback_data='contact')]
        ])
    )
    return ConversationHandler.END
