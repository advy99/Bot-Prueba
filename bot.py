from telegram.ext import Updater, CommandHandler
from config import TOKEN

def saludar(bot, update):
    update.message.reply_text(
        'Hola {}'.format(update.message.from_user.first_name))


def palindromo(bot, update):
	texto = update.message.reply_to_message.text

	if(texto == texto[::-1]):
		update.message.reply_text(
			'El texto: " {} " es un palindromo'.format(texto))
	else:
		update.message.reply_text(
			'El texto: " {} " no es un palindromo'.format(texto))



updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', saludar))

updater.dispatcher.add_handler(CommandHandler('palindromo',palindromo))

updater.start_polling()
updater.idle()
