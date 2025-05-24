import telebot
import webbrowser
bot = telebot.TeleBot('8034006021:AAFvaWnAUg70xucbRtxtEUxQd2GqbjeJcE4')

@bot.message_handler(commands=['start']) 
#  получая от пользователя старт, выполняем функцию снизу
def main(message):
    #  message может иметь любое имя. обязательно под хендлером
    # стоит его функция
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, го секс?')
    # говорит отправить соо (из чата, который написал старт)

bot.infinity_polling()
# делает, чтобы он работал нонстоп
    
    