import telebot
import sqlite3

bot = telebot.TeleBot('8034006021:AAFvaWnAUg70xucbRtxtEUxQd2GqbjeJcE4')
@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('nandomo.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primery key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегестрируем')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    pass

bot.remove_webhook()
bot.polling(none_stop=True)
    
    