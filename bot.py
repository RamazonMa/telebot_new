import logging
import wikipedia
import telebot

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2009259081:AAE3p6OXbR4XPpW-k0N9bqe-Hq6JJrFqUQg'
wikipedia.set_lang('[uz]' & '[ru]')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# @dp.message_handler(commands=['start'])
# def start(message):
#     name = str(message.from_user.first_name)
#     bot.send_message(message.from_user.id, 'Assalom aleykum ' + name)
#

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    name = str(message.from_user.full_name)
    await bot.send_message(message.from_user.id, 'Assalom aleykum ' + name)


@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid topilmadi yuq karochisi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
