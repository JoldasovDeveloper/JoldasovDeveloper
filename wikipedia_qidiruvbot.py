import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1998265795:AAHfGlLwlfghBi9yEgcs4ixQl1lGQuva9bE'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom!👋 Men Wikipedia tarmog'idan sizga kerakli bo'lgan maqolani topishga harakat qilaman!\nSizga qaysi maqolani topib beray?🤔 Menga matn yuboring!")

@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Kechirasiz😕 Biz bu matnga oid maqolani topa olmadik?!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)