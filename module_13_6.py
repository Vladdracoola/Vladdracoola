from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Filter, Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

api = ''


class TextFilter(Filter):
    def __init__(self, text: str):
        self.text = text

    async def __call__(self, message: types.Message) -> bool:
        return message.text == self.text


kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')]],
    resize_keyboard=True)

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='count'),
         InlineKeyboardButton(text='Формулы расчёта', callback_data='formula')]],
    resize_keyboard=True)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


def register_handlers(dp: Dispatcher):
    @dp.message(TextFilter('Рассчитать'))
    async def set_age(message: types.Message, state: FSMContext):
        await message.answer('Выбери опцию:', reply_markup=inline_kb)
        await state.set_state(UserState.age)

    @dp.callback_query(lambda call: call.data == 'count')
    async def inform(call: types.CallbackQuery, state: FSMContext):
        await call.message.answer('Введите свой возраст')
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

    @dp.message(Command('start'))
    async def start_message(message: types.Message):
        await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

    @dp.message(TextFilter('Информация'))
    async def set_age(message: types.Message):
        await message.answer('Этот бот поможет вам узнать свою суточную норму калорий, '
                             'согласно упрощенной формуле Миффлина - Сан-Жеора. '
                             'Нажмите "Рассчитать", а затем следуйте инструкциям бота.')

    @dp.callback_query(lambda call: call.data == 'formula')
    async def inform(call: types.CallbackQuery):
        await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
        await call.answer()

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
