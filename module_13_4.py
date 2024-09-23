from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Filter
import asyncio

api = ''


class TextFilter(Filter):
    def __init__(self, text: str):
        self.text = text

    async def __call__(self, message: types.Message) -> bool:
        return message.text == self.text


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


def register_handlers(dp: Dispatcher):
    @dp.message(TextFilter('Calories'))
    async def set_age(message: types.Message, state: FSMContext):
        await message.answer('Введите свой возраст')
        await state.set_state(UserState.age)

    @dp.message(UserState.age)
    async def set_growth(message: types.Message, state: FSMContext):
        await state.update_data(age=message.text)
        await message.answer('Введите свой рост:')
        await state.set_state(UserState.growth)

    @dp.message(UserState.growth)
    async def set_weight(message: types.Message, state: FSMContext):
        await state.update_data(growth=message.text)
        await message.answer('Введите свой вес:')
        await state.set_state(UserState.weight)

    @dp.message(UserState.weight)
    async def send_calories(message: types.Message, state: FSMContext):
        await state.update_data(weight=message.text)
        data = await state.get_data()
        calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) + 5
        await message.answer(f'Ваша дневная норма калорий: {calories}')
        await state.clear()


async def main():
    bot = Bot(token=api)
    dp = Dispatcher(storage=MemoryStorage())
    register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
