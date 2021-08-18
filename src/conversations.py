from telegram import Update
from telegram.ext import ConversationHandler

import constants


def first_name_conversation(update: Update, context):
    query = update.callback_query
    print('query', query)
    query.answer()

    query.message.reply_text(text='Por favor introduzca el nombre:')
    return constants.INPUT_LAST_NAME


def last_name_conversation(update, context):
    query = update.callback_query
    text = query.message.text
    print('text')
    query.answer()

    query.message.reply_text(text='Por favor introduzca el Apellido:')
    return constants.INPUT_PHONE


def phone_conversation(update, context):
    query = update.callback_query
    text = query.message.text
    print(text)
    query.answer()

    query.message.reply_text(text='Por favor introduzca su numero de telefono:')
    return constants.SAVE_INFO


def save_info_conversation(update, context):
    query = update.callback_query
    query.answer()

    # guardar la información
    query.message.reply_text('Su información ha sido guardada con éxito')
    return ConversationHandler.END
