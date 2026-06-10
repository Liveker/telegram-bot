import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = 8673377484:AAE5DgixFrPWSKcvjDPF_PSokm9FMdgjRhk

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Я твой генератор AI")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
