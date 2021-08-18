from telegram import Update


def contact_callback(update: Update, context):
    query = update.callback_query
    query.answer()

    query.message.reply_text(text='dale')
