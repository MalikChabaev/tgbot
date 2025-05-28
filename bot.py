import telebot
import requests
import json

bot = telebot.TeleBot('8034006021:AAFvaWnAUg70xucbRtxtEUxQd2GqbjeJcE4')
API = '7cd03fb8c220cb871ca5331a21952afa'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        'Привет, рад тебя видеть! ☀️\nНапиши название города, который тебя интересует 🌍'
    )

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric&lang=ru'
    )
    
    if res.status_code == 200:
        data = res.json()
        temp = data["main"]["temp"]
        weather_main = data["weather"][0]["main"]
        weather_desc = data["weather"][0]["description"]

        # Подбор совета по температуре
        if temp >= 30:
            advice = "Очень жарко! Надень кепку, пей воду и избегай солнца ☀️🧢💦"
        elif temp >= 20:
            advice = "Тепло и приятно! Отличная погода для прогулки 😎🌳"
        elif temp >= 10:
            advice = "Прохладно. Лучше накинуть курточку 🧥🍂"
        elif temp >= 0:
            advice = "Холодновато. Теплее одевайся и бери шарф 🧣❄️"
        else:
            advice = "Очень холодно! Надень шапку, перчатки и держись тепла 🥶🧤🧊"

        # Предупреждение о дожде
        if weather_main in ["Rain", "Drizzle"]:
            advice += "\n☔️ Похоже, будет дождь. Не забудь зонт!"

        bot.reply_to(message, f"🌡 В городе {city.title()} сейчас {temp}°C, {weather_desc}.\n{advice}")
    else:
        bot.reply_to(message, f"❗️Не удалось найти город '{city}'. Попробуй ещё раз.")

bot.remove_webhook()
bot.polling(none_stop=True)
