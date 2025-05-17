import telebot

BOT_TOKEN = '8165091886:AAGfa7wf30JJRVN6wYkh9Ail-8y20np_tpY'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()