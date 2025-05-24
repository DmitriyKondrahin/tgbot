import telebot
import keyboard
import fsm

BOT_TOKEN = '8165091886:AAGfa7wf30JJRVN6wYkh9Ail-8y20np_tpY'
starter = fsm.FSM()
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def on_message(message):
    msg_text = message.text
    state = starter.get_state(message.chat.id)
    if state == fsm.def_st:
        if msg_text == "Фото🖼️":
            starter.set_state(message.chat.id, fsm.img_st)
            bot.send_message(message.chat.id, text="Напиши описание фото", reply_markup=keyboards.back)
        elif msg_text == "Текст":
            starter.set_state(message.chat.id, fsm.text_st)
            bot.send_message(message.chat.id, text="Напиши то, о чём хочешь спросить", reply_markup=keyboards.back)
        else:
            bot.send_message(message.chat.id, text="Я не понимаю вашей команды...", reply_markup=keyboards.start)
    elif state == fsm.img_st:
        if msg_text == "В меню":
            starter.set_state(message.chat.id, fsm.def_st)
            bot.send_message(message.chat.id, text="Главное меню", reply_markup=keyboards.start)
        else:
            bot.send_message(message.chat.id, text="Скоро буду генерировать фото...")
    elif state == fsm.text_st:
        starter.set_state(message.chat.id, fsm.def_st)
        bot.send_message(message.chat.id, text="Я не понимаю вашей команды...", reply_markup=keyboards.start)

bot.polling()