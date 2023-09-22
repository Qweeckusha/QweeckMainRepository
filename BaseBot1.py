from aiogram import Dispatcher, executor, Bot, types
import requests
import datetime
import config

bot = Bot(config.BOT_TOKEN)
api = 'd031223335de6838db57720ffedbeb2b'
dp = Dispatcher(bot)
joinedFile = open('joined_users.txt')
JoinedUsers = set()

# проверка файла на наличие ID в основном файле с ID
for line in joinedFile:
    JoinedUsers.add(line.strip())
joinedFile.close()

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer('Привет! \nЭтот бот создан для тренировки и практики, чтобы ознакомиться с его командами, используй /help')
    if not str(msg.chat.id) in JoinedUsers:
        joinedFile = open('joined_users.txt', 'a')
        joinedFile.write(str(msg.chat.id) + '\n')
        JoinedUsers.add(msg.chat.id)
    await msg.answer('Вы наш посетитель.')

@dp.message_handler(commands=['help'])
async def help(msg: types.Message):
    await msg.answer('/start - Начало бота \n/help - Этот список \n/weather - погода в твоём городе')

@dp.message_handler(commands=['info'])
async def info(msg: types.Message):
    await msg.answer('Данный бот представляет собой базу, которая способна выполнять стандартный пакет функций. '
                     'В дальнейшем этот бот может стать эффективнее')

@dp.message_handler(commands=['scrt'])
async def mes(msg: types.Message):
    for user in JoinedUsers:
        await bot.send_message(user, msg.text[msg.text.find(' '):])

@dp.message_handler(commands=['weather'])
async def weather(msg: types.Message):
    await msg.answer('Вы выбрали режим сводки о погоде. Напишите название города, о погоде которого хотите получить информацию☀🌦⛅')

@dp.message_handler(content_types=['text'])
async def get_weather(msg: types.Message):
    try:
        city = msg.text.strip().lower()
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
        data = r.json()
        cityjson = data["name"]
        temp = data["main"]["temp"]
        wind = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M')
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M')
        code_to_smile = {                                                               
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B",
            "light rain": "Пасмурно 🌧"
        }
        weather_desc = data["weather"][0]["description"]
        if weather_desc in code_to_smile:
            wd = code_to_smile[weather_desc]
        else:
            wd = 'Выгляните в окно, я не понимаю, что там за погода😔'
        await msg.reply(f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M')} \n"
        f'Город: {city} \nТемпература {temp}℃ {wd}\n'
        f'Влажность: {humidity}% 💧\nСкорость ветра: {wind} м/с 💨\n'
        f'Время восхода: {sunrise} 🌅\nВремя заката: {sunset} 🎑'
        )
    except:
        await msg.answer('Вы неправильно ввели название города. Попробуйте снова.')


'''Попробовать сделать условие, чтобы температура меняла смайлик на комфорт, жарко и холодно'''

executor.start_polling(dp)