from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Рассчитать'),
               KeyboardButton(text='Информация')]
              ],
    resize_keyboard=True
)

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Мужской', callback_data='male'),
         InlineKeyboardButton(text='Женский', callback_data='female')]
    ],
    resize_keyboard=True
)

inline_kb2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Низкий', callback_data='low'),
         InlineKeyboardButton(text='Средний', callback_data='med'),
         InlineKeyboardButton(text='Высокий', callback_data='high')]
    ],
    resize_keyboard=True
)
