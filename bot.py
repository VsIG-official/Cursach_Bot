import telebot
import Config
import random

from telebot import types

bot = telebot.TeleBot(Config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Матан")
    item2=types.KeyboardButton("Англ")

    markup.add(item1,item2)
    bot.send_message(message.chat.id,"Привіт, <b>ЯкеБулоДЗ-кун/тян</b>. Я ДЗ-бот. Моя ціль - <s>захопити весь світ</s> дати дз, яке Тобі потрібно".format(message.from_user, bot.get_me()),
    parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Матан':
            bot.send_message(message.chat.id, "Лови матан")
        elif message.text == 'Англ':
            bot.send_message(message.chat.id, "Лови англ")
        else:
            bot.send_message(message.chat.id, "Я впав")

#RUN
bot.polling(none_stop=True)