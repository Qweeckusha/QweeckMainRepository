import telebot
import requests
import json

bot = telebot.TeleBot('6664259900:AAH_0VUD4wOQu_EDQzneVZwcACkXAyz6WVA')
api = 'd031223335de6838db57720ffedbeb2b'

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, 'Привет! Можешь написать навание своего города и я найду информацию о погоде в нём☀🌦⛅')

@bot.message_handler(content_types=['text'])
def get_weather(msg):
    city = msg.text.strip().lower()
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    if r.status_code == 200:
        data = json.loads(r.text)
        t_min = data["main"]["temp_min"]
        t_max = data["main"]["temp_max"]
        bot.reply_to(msg, f'Температура: от {t_min}℃ до {t_max}℃' if t_min != t_max else f'Температура: {t_max}℃')
    else:
        bot.reply_to(msg, 'Такого города не существует или его название введено неверно😔😔😕')

#def weather(msg):
bot.polling(none_stop=True)