from telegram.ext import Updater, CommandHandler
from config import TOKEN
import utils

def saludar(bot, update):
    update.message.reply_text(
        'Hola {}'.format(update.message.from_user.first_name))

def sed(bot, update):
    update.message.reply_text(
        'Si no bebo agua meahfisio, {}'.format(update.message.from_user.first_name))


def palindromo(bot, update):
	# message.text format "/command text"
	tmp = update.message.text.split(" ")

	# first element is command
	tmp.pop(0)
	# tebuild text back to its form
	msg = ' '.join(tmp)

	if msg is not "":
		utils.is_palindrome(bot, update, msg)
	else:
		update.message.reply_text("Prueba de nuevo.")


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', saludar))

updater.dispatcher.add_handler(CommandHandler('palindromo',palindromo))

updater.dispatcher.add_handler(CommandHandler('sed', sed))

updater.start_polling()
updater.idle()
