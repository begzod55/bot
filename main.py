import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

wikipedia.set_lang('uz')

API_TOKEN = '7579893508:AAHxBzjeG92bJ4rF8Pvc1sy3atax4Zuavkw'  # <-- Bu yerga o'zingizning bot tokeningizni yozing

# Loglarni sozlash
logging.basicConfig(level=logging.INFO)

# Bot va dispatcher'ni ishga tushirish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# /start yoki /help komandasi yuborilganda ishlovchi handler
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    Bu funksiya foydalanuvchi /start yuborganida chaqiriladi
    """
    await message.reply("Assalomu alaykum! bot haqida /help")

@dp.message_handler(commands=['help'])
async def send_help(message: types.message):
    """
    Bu funksiya foydalanuvchi /help yuborganida chaqiriladi
    """
    await message.reply("Har qanday xabarni ma'lumotlarini topib sizga yuboriladi. Agar siz topmoqchi bo'lgan ma'lumot topilmasa yuborgan xabaringini to'g'riligini tekshiring!! ")

@dp.message_handler(commands=['owner'])
async def send_help(message: types.message):
    """
    Bu funksiya foydalanuvchi /help yuborganida chaqiriladi
    """
    await message.reply("Bu botning yaratuvchisi @begzod_131")

@dp.message_handler(commands=['bots'])
async def send_help(message: types.message):
    """
    Bu funksiya foydalanuvchi /help yuborganida chaqiriladi
    """
    await message.reply("hali botlar mavjud emas")


# Har qanday xabarni ma'lumotlarini yubradi agarda habar haqida malumot yoq bolsa 'bu mavzuga oida ma'lumot topilmadi'
@dp.message_handler()
async def wikisend(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("bu mavzuga oida ma'lumot topilmadi")



# Botni ishga tushirish
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)