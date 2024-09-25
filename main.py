from aiogram import Bot, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import asyncio

from config import *
from keyboards import *


def register_handlers(dp: Dispatcher):
    @dp.message(UserState.weight)
    async def send_calories(message: types.Message, state: FSMContext):
        await state.update_data(weight=message.text)
        data = await state.get_data()
        if data['gender'] == 'Мужской':
            calories = round((
                10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) + 5) * float(
                data['activity']))
            await message.answer(f'Ваша дневная норма калорий: {calories}')
        else:
            calories = round((
                10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) - 161) * float(
                data['activity']))
            await message.answer(f'Ваша дневная норма калорий: {calories}')
        await state.clear()

    @dp.message(UserState.growth)
    async def set_weight(message: types.Message, state: FSMContext):
        await state.update_data(growth=message.text)
        await message.answer('Введите свой вес:')
        await state.set_state(UserState.weight)

    @dp.message(UserState.age)
    async def set_growth(message: types.Message, state: FSMContext):
        await state.update_data(age=message.text)
        await message.answer('Введите свой рост:')
        await state.set_state(UserState.growth)

    @dp.callback_query(lambda call: call.data in ['male', 'female'])
    async def set_age(call: types.CallbackQuery, state: FSMContext):
        if call.data == 'male':
            await state.update_data(gender='Мужской')
        elif call.data == 'female':
            await state.update_data(gender='Женский')
        await call.message.answer('Введите свой возраст')
        await state.set_state(UserState.age)

    @dp.callback_query(lambda call: call.data in ['low', 'med', 'high'])
    async def set_gender(call: types.CallbackQuery, state: FSMContext):
        if call.data == 'low':
            await state.update_data(activity=1.375)
        elif call.data == 'med':
            await state.update_data(activity=1.55)
        elif call.data == 'high':
            await state.update_data(activity=1.725)
        await call.message.answer('Укажите ваш пол:', reply_markup=inline_kb)
        await state.set_state(UserState.gender)

    @dp.message(TextFilter('Рассчитать'))
    async def set_activity(message: types.Message, state: FSMContext):
        await message.answer('Укажите ваш уровень активности', reply_markup=inline_kb2)
        await state.set_state(UserState.activity)

    @dp.message(TextFilter('Информация'))
    async def inform(message: types.Message):
        await message.answer('Этот бот поможет вам узнать суточную норму калорий, '
                             'согласно формуле Миффлина - Сан-Жеора. '
                             'Нажмите "Рассчитать", а затем следуйте инструкциям бота.')

    @dp.message(Command('start'))
    async def start_message(message: types.Message):
        await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

    @dp.message()
    async def all_massages(message: types.Message):
        await message.answer('Введите команду /start, чтобы начать общение.')


async def main():
    bot = Bot(token=api)
    dp = Dispatcher(storage=MemoryStorage())
    register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
