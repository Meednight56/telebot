# Импорт библиотек

import telebot 
import requests 
from telebot import types

# Создание бота

bot = telebot.TeleBot("8027158453:AAGqM0kzKxK2AX_p__xb5rh5nZw2xsLBlpw")

# Старт

@bot.message_handler(commands=["start"])
def start(m, res=False):

# Кнопки

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    button1 = types.KeyboardButton("Факт")
    button2 = types.KeyboardButton("Шутка")
    markup.add(button1)
    markup.add(button2)
    bot.send_message(m.chat.id, "Привет! Я - твой интерактивный бот для развлечения.\nНажми: \nФакт - для получения интересного факта\nШутка - для получения шутки", reply_markup=markup)

# Сообщение от пользователя - Факт

@bot.message_handler(func=lambda message: message.text == 'Факт')
def get_fact(message):
        url_fact = "http://numbersapi.com/random/trivia"
        response = requests.get(url_fact)
        if response.status_code == 200:
            data = response.text
            bot.send_message(message.chat.id, data)

# Сообщение от пользователя - Шутка

@bot.message_handler(func=lambda message: message.text == 'Шутка')
def get_joke(message):
        url_joke = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url_joke)
        if response.status_code == 200:
            data = response.json()
            joke = f"{data['setup']}\n\n{data['punchline']}"
            bot.send_message(message.chat.id, joke)

# Запуск бота
            
if __name__ == '__main__':
    print("Бот успешно запущен")          
    bot.polling(none_stop=True, interval=0)             
    