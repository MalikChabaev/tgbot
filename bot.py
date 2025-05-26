import telebot
import sqlite3

bot = telebot.TeleBot('8034006021:AAFvaWnAUg70xucbRtxtEUxQd2GqbjeJcE4')
name = None

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
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_name)
    
def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('nandomo.sql')
    cur = conn.cursor()

    cur.execute(
        f'INSERT INTO users (name, pass) VALUES ({name}, {password})'
        )
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегестрирован', reply_markup=markup)
    # bot.register_next_step_handler(message, user_name)

bot.remove_webhook()
bot.polling(none_stop=True)
    
    