from telegram.ext import Updater, CommandHandler
from config import TOKEN

def saludar(bot, update):
    update.message.reply_text(
        'Hola {}'.format(update.message.from_user.first_name))


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', saludar))

updater.start_polling()
updater.idle()
