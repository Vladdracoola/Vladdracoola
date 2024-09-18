from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import asyncio

api = ''


def register_handlers(dp: Dispatcher):
    @dp.message(Command('start'))
    async def start_message(message):
        await message.answer('Привет! Я бот помогающий твоему здоровью.')

    @dp.message()
    async def all_massages(message):
        await message.answer('Введите команду /start, чтобы начать общение.')


async def main():
    bot = Bot(token=api)
    dp = Dispatcher(storage=MemoryStorage())
    register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
