from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import TOKEN
import logging

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

def palindromo(bot, update):
	# call the bot like this:
	# /palindromo radar
	texto = update.message.text.replace('/palindromo ', '').strip()

	if(texto == texto[::-1]):
		update.message.reply_text(
			'El texto: " {} " es un palindromo'.format(texto))
	else:
		update.message.reply_text(
			'El texto: " {} " no es un palindromo'.format(texto))

def owo(bot, update):
    update.message.reply_text(
        'OwO whats this? {}'.format(update.message.from_user.first_name))

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


	# Handler de errores:
	dp.add_error_handler(error)

	# Iniciar el bot:
	updater.start_polling()

	# Tener el bot activado hasta que se detenga con Ctrl+c:
	updater.idle()

if __name__ == '__main__':
	main()
