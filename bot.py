# -*- coding: utf-8 -*-

import logging
from config import TOKEN
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
						  ConversationHandler, RegexHandler)
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
import utils

# Habilitar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def saludar(bot, update):
    update.message.reply_text(
        'Hola {}'.format(update.message.from_user.first_name))

def sed(bot, update):
    update.message.reply_text(
        'Si no bebo agua meahfisio, {}'.format(update.message.from_user.first_name))

def catastrofe(bot, update):
    update.message.reply_text(
        '¡¡¡¡¡{}, esto es una catastrófe!!!!!!'.format(update.message.from_user.first_name))

def amigo (bot, update):
	chat_id = update.message.chat_id
	msg= update.message.text.lower()
	if 'amigo' in msg or 'friend' in msg :
		bot.send_photo(chat_id, "https://www.articulosreligiososbrabander.es/uploads/media/images/396x396/imagen-artesanal-del-nino-jesus-con-panales-para-cuna-11.jpg", "This is my amazing new friend!.")

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
def owo(bot, update):
    update.message.reply_text(
        'OwO whats this? {}'.format(update.message.from_user.first_name))

# Never gives you up:
def navidad(bot, update):
	user = update.message.from_user
	chat_id = update.message.chat_id
	logger.info("Feliz Navidad, {} !.".format(user.first_name))

	# Send the video:
	update.message.reply_text("https://www.youtube.com/watch?v=dx_ZhonlxHU")

# Error handler
def error(bot, update, error):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, error)

def main():
	# Iniciar el bot
	# Crear el EventHandler y pasarle el TOKEN de nuestro bot:
	updater = Updater(TOKEN)

	# Hacer que el dispatcher registre los handlers:
	dp = updater.dispatcher

	# Comandos:
	dp.add_handler(CommandHandler('start', saludar))
	dp.add_handler(CommandHandler('palindromo', palindromo))
	dp.add_handler(CommandHandler('sed', sed))
	dp.add_handler(CommandHandler('catastrofe', catastrofe))
	dp.add_handler(CommandHandler('owo', owo))
	dp.add_handler(CommandHandler('navidad', navidad))

	dp.add_handler(MessageHandler(Filters.text, amigo))


	# Handler de errores:
	dp.add_error_handler(error)

	# Iniciar el bot:
	updater.start_polling()

	# Tener el bot activado hasta que se detenga con Ctrl+c:
	updater.idle()

if __name__ == '__main__':
	main()
