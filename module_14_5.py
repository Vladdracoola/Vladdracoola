from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Filter, Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, FSInputFile
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from crud_functions import *

api = ''


class TextFilter(Filter):
    def __init__(self, text: str):
        self.text = text

    async def __call__(self, message: types.Message) -> bool:
        return message.text == self.text


kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Рассчитать'),
               KeyboardButton(text='Информация')],
              [KeyboardButton(text='Купить'),
               KeyboardButton(text='Регистрация')]],
    resize_keyboard=True)

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='count'),
         InlineKeyboardButton(text='Формулы расчёта', callback_data='formula')]],
    resize_keyboard=True)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data="product_buying"),
         InlineKeyboardButton(text='Product2', callback_data="product_buying"),
         InlineKeyboardButton(text='Product3', callback_data="product_buying"),
         InlineKeyboardButton(text='Product4', callback_data="product_buying")]],
    resize_keyboard=True)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


def register_users(dp: Dispatcher):
    @dp.message(TextFilter('Регистрация'))
    async def sing_up(message: types.Message, state: FSMContext):
        await message.answer('Введите имя пользователя (только латинский алфавит):')
        await state.set_state(RegistrationState.username)

    @dp.message(RegistrationState.username)
    async def set_username(message: types.Message, state: FSMContext):
        await state.update_data(username=message.text)
        if is_included(message.text):
            await message.answer('Пользователь существует, введите другое имя')
            return
        await message.answer('Введите свой email')
        await state.set_state(RegistrationState.email)

    @dp.message(RegistrationState.email)
    async def set_email(message: types.Message, state: FSMContext):
        await state.update_data(email=message.text)
        await message.answer('Введите свой возраст')
        await state.set_state(RegistrationState.age)

    @dp.message(RegistrationState.age)
    async def set_age(message: types.Message, state: FSMContext):
        await state.update_data(age=message.text)
        user_data = await state.get_data()
        username = user_data['username']
        email = user_data['email']
        age = user_data['age']
        add_user(username, email, age)
        await message.answer('Регистрация прошла успешно!', reply_markup=kb)
        await state.clear()


def register_handlers(dp: Dispatcher):
    @dp.message(TextFilter('Рассчитать'))
    async def option(message: types.Message):
        await message.answer('Выбери опцию:', reply_markup=inline_kb)

    @dp.message(TextFilter('Купить'))
    async def get_buying_list(message: types.Message):
        products = get_all_products()
        photos = [
            '',
            '',
            '',
            ''
        ]
        for i, product in enumerate(products):
            product_id, title, description, price = product
            img = FSInputFile(photos[i])
            await message.answer_photo(photo=img,
                                       caption=f'Название: {title} | Описание: {description} |'
                                               f' Цена: {price}')
        await message.answer('Выберите продукт для покупки:', reply_markup=buy_kb)

    @dp.callback_query(lambda call: call.data == 'product_buying')
    async def send_confirm_message(call: types.CallbackQuery):
        await call.message.answer('Вы успешно приобрели продукт!')
        await call.answer()

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
    async def info(message: types.Message):
        await message.answer('Этот бот поможет вам узнать свою суточную норму калорий, '
                             'согласно упрощенной формуле Миффлина - Сан-Жеора. '
                             'Нажмите "Рассчитать", а затем следуйте инструкциям бота.')

    @dp.callback_query(lambda call: call.data == 'formula')
    async def formula(call: types.CallbackQuery):
        await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
        await call.answer()

    @dp.message()
    async def all_massages(message: types.Message):
        await message.answer('Введите команду /start, чтобы начать общение.')


async def main():
    bot = Bot(token=api)
    dp = Dispatcher(storage=MemoryStorage())
    register_users(dp)
    register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
