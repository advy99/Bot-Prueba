from telegram.ext import Updater, CommandHandler
from config import TOKEN

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
	texto = update.message.reply_to_message.text

	if(texto == texto[::-1]):
		update.message.reply_text(
			'El texto: " {} " es un palindromo'.format(texto))
	else:
		update.message.reply_text(
			'El texto: " {} " no es un palindromo'.format(texto))
		
def owo(bot, update):
    update.message.reply_text(
        'OwO whats this? {}'.format(update.message.from_user.first_name))



updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', saludar))

updater.dispatcher.add_handler(CommandHandler('palindromo',palindromo))

updater.dispatcher.add_handler(CommandHandler('sed', sed))

updater.dispatcher.add_handler(CommandHandler('catastrofe',catastrofe))

updater.dispatcher.add_handler(CommandHandler('owo',owo))

updater.start_polling()
updater.idle()
