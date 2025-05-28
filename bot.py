import telebot
import sqlite3

bot = telebot.TeleBot('8034006021:AAFvaWnAUg70xucbRtxtEUxQd2GqbjeJcE4')
name = None

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города, который тебя интересует')

bot.remove_webhook()
bot.polling(none_stop=True)
