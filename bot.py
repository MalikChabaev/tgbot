import telebot
import requests
bot = telebot.TeleBot('8034006021:AAFvaWnAUg70xucbRtxtEUxQd2GqbjeJcE4')
API = '7cd03fb8c220cb871ca5331a21952afa'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города, который тебя интересует')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    bot.reply_to(message, f'Сейчас погода: {res.json()}')

bot.remove_webhook()
bot.polling(none_stop=True)
