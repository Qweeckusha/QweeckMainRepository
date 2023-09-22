# from aiogram import Dispatcher, Bot, executor, types
#
# bot = Bot('BOT_TOKEN')
# dp = Dispatcher(bot)
#
#
#
# executor.start_polling(dp)
from aiogram import Dispatcher, Bot, executor, types
import config
from aiogram.utils.callback_data import CallbackData

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)

cd = CallbackData('item', 'msg')

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer(f'Привет {msg.from_user.first_name}\nВы можете выбрать свой товар в списке /list.')
    # await bot.send_invoice(msg.chat.id, 'На водичку.', 'Донат 70 рублей на акваминерале', 'invoice', config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Водичка', 70*100)])

@dp.message_handler(content_types=types.ContentTypes.SUCCESSFUL_PAYMENT)
async def payment(msg: types.Message):
    await msg.answer(f'Платеж прошёл успешно.\nИнформация о платеже: {msg.successful_payment.order_info}\n'
                     f'Ваш уникальный ID:{msg.successful_payment.shipping_option_id}')

@dp.message_handler(commands=['list'])
async def list(msg: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    btn1 = markup.add(types.InlineKeyboardButton('1000 Wood', callback_data='wood1'))
    btn2 = markup.add(types.InlineKeyboardButton('2000 Wood', callback_data='wood2'))
    btn3 = markup.add(types.InlineKeyboardButton('3000 Wood', callback_data='wood3'))
    btn4 = markup.add(types.InlineKeyboardButton('Next page 1/3', callback_data='np'))
    await msg.answer('Выберите товар.', reply_markup=markup)

@dp.message_handler(commands=['list'])
async def list1(msg: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = markup.add(types.InlineKeyboardButton('1000 Wood', callback_data='wood1'))
    btn2 = markup.add(types.InlineKeyboardButton('2000 Wood', callback_data='wood2'))
    btn3 = markup.add(types.InlineKeyboardButton('3000 Wood', callback_data='wood3'))
    btn4 = markup.add(types.InlineKeyboardButton('Next page 1/3', callback_data='np'))
    await bot.edit_message_reply_markup(chat_id=msg.chat.id, message_id=msg.message_id, reply_markup=markup)
@dp.message_handler(commands=['list2'])
async def list2(msg: types.Message):
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    btn1 = markup2.add(types.InlineKeyboardButton('1000 stone', callback_data='stone1'))
    btn2 = markup2.add(types.InlineKeyboardButton('2000 stone', callback_data='stone2'))
    btn3 = markup2.add(types.InlineKeyboardButton('3000 stone', callback_data='stone3'))
    btn4 = markup2.add(types.InlineKeyboardButton('Next page 2/3', callback_data='np2'))
    await bot.edit_message_reply_markup(chat_id=msg.chat.id, message_id=msg.message_id,reply_markup=markup2)

@dp.message_handler(commands=['list3'])
async def list3(msg: types.Message):
    markup3 = types.InlineKeyboardMarkup(row_width=2)
    btn1 = markup3.add(types.InlineKeyboardButton('1000 iron', callback_data='iron1'))
    btn2 = markup3.add(types.InlineKeyboardButton('2000 iron', callback_data='iron2'))
    btn3 = markup3.add(types.InlineKeyboardButton('3000 iron', callback_data='iron3'))
    btn4 = markup3.add(types.InlineKeyboardButton('Next page 3/3', callback_data='fp'))
    await bot.edit_message_reply_markup(chat_id=msg.chat.id, message_id=msg.message_id,reply_markup=markup3)

@dp.callback_query_handler()
async def call(call):
    if call.data == 'wood1':
        await bot.send_invoice(call.message.chat.id, 'Wood', 'Buy 1000 wood', 'invoice',
                                config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Wood', 99 * 100)])
    if call.data == 'wood2':
        await bot.send_invoice(call.message.chat.id, 'Wood', 'Buy 2000 wood', 'invoice',
                               config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Wood', 199 * 100)])
    if call.data == 'wood3':
        await bot.send_invoice(call.message.chat.id, 'Wood', 'Buy 3000 wood', 'invoice',
                               config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Wood', 299 * 100)])
    if call.data == 'np':
        await list2(call.message)

    # Обработка второй страницы
    if call.data == 'stone1':
        await bot.send_invoice(call.message.chat.id, 'Stone', 'Buy 1000 stone', 'invoice',
                                config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Stone', 199 * 100)])
    if call.data == 'stone2':
        await bot.send_invoice(call.message.chat.id, 'Stone', 'Buy 2000 stone', 'invoice',
                               config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Wood', 299 * 100)])
    if call.data == 'stone3':
        await bot.send_invoice(call.message.chat.id, 'Stone', 'Buy 3000 stone', 'invoice',
                               config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Wood', 399 * 100)])
    if call.data == 'np2':
        await list3(call.message)

    # Обработка третьей страницы
    if call.data == 'iron1':
        await bot.send_invoice(call.message.chat.id, 'Iron', 'Buy 1000 iron', 'invoice',
                                config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Iron', 299 * 100)])
    if call.data == 'iron2':
        await bot.send_invoice(call.message.chat.id, 'Iron', 'Buy 2000 iron', 'invoice',
                               config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Iron', 399 * 100)])
    if call.data == 'iron3':
        await bot.send_invoice(call.message.chat.id, 'Iron', 'Buy 3000 iron', 'invoice',
                               config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Iron', 499 * 100)])
    if call.data == 'fp':
        await list1(call.message)


# @dp.callback_query_handler()
# async def calllist2(call):
#     if call.data == 'stone1':
#         await bot.send_invoice(call.message.chat.id, 'Stone', 'Buy 1000 stone', 'invoice',
#                                 config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Stone', 99 * 100)])
#     if call.data == 'stone2':
#         await bot.send_invoice(call.message.chat.id, 'Stone', 'Buy 2000 stone', 'invoice',
#                                config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Wood', 199 * 100)])
#     if call.data == 'stone3':
#         await bot.send_invoice(call.message.chat.id, 'Stone', 'Buy 3000 stone', 'invoice',
#                                config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Wood', 299 * 100)])


# @dp.callback_query_handler()
# async def call2(call):
#     if call.data == 'stone1':
#         await bot.send_invoice(call.message.chat.id, 'Stone', 'Buy 1000 stone', 'invoice',
#                                 config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Wood', 99 * 100)])
#     if call.data == 'wood2':
#         await bot.send_invoice(call.message.chat.id, 'Wood', 'Buy 2000 wood', 'invoice',
#                                config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Wood', 199 * 100)])
#     if call.data == 'wood3':
#         await bot.send_invoice(call.message.chat.id, 'Wood', 'Buy 3000 wood', 'invoice',
#                                config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Wood', 299 * 100)])

executor.start_polling(dp)