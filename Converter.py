import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('6664259900:AAH_0VUD4wOQu_EDQzneVZwcACkXAyz6WVA')
currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, 'Привет! Введите сумму для конвертации.')
    bot.register_next_step_handler(msg, summa)

def summa(msg):
    global amount
    try:
        amount = int(msg.text.strip())
    except ValueError:
        bot.send_message(msg.chat.id, 'Неверный формат, введите сумму для конвертации.')
        '''Полезное отслеживание ошибок кода'''
        bot.register_next_step_handler(msg,summa)
        return
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        b1 = types.InlineKeyboardButton('USD/RUB', callback_data='usd/rub')
        b2 = types.InlineKeyboardButton('RUB/USD', callback_data='rub/usd')
        b3 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        b4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
        markup.add(b1,b2,b3,b4)
        bot.send_message(msg.chat.id, 'Выберите пару валют', reply_markup=markup)
    else:
        bot.send_message(msg.chat.id, 'Dведите сумму для конвертации больше 0.')
        bot.register_next_step_handler(msg, summa)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        val = call.data.upper().split('/')
        res = currency.convert(amount, val[0], val[1])
        bot.send_message(call.message.chat.id, f'Получается {round(res, 2)}. Можете заново вписать сумму.')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Введите два значения через "/"')
        bot.register_next_step_handler(call.message, my_currency)
        
def my_currency(msg):
    val = call.data.upper().split('/')
    res = currency.convert(amount, val[0], val[1])
    bot.send_message(call.message.chat.id, f'Получается {round(res, 2)}. Можете заново вписать сумму.')


bot.polling(none_stop=True)