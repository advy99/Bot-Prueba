# Utilities for the bot:

# Check if a word is a palindrome:
def is_palindrome(bot, update, text):

	if text == text[::-1]:
		message = 'El texto "{}" es un  palíndromo'.format(text)
	else:
		message = 'El texto "{}" no es un palíndromo'.format(text)
	update.message.reply_text(message)
