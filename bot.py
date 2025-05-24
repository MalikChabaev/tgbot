import telebot

bot = telebot.TeleBot('8034006021:AAFvaWnAUg70xucbRtxtEUxQd2GqbjeJcE4')

@bot.message_handler(commands=['start', 'end']) 
def handle_commands(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, привет!')

bot.remove_webhook()         # Удаляем webhook, если он был
bot.infinity_polling()       # Запускаем polling, бот работает непрерывно

    
    