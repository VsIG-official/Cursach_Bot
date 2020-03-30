import telebot
import Config

bot = telebot.TeleBot(Config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Привіт, <b>ЯкеБулоДЗ-кун/тян</b>. Я ДЗ-бот. Моя ціль - <s>захопити весь світ</s> дати дз, яке Тобі потрібно".format(message.from_user, bot.get_me()),
    parse_mode='html')

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)

#RUN
bot.polling(none_stop=True)