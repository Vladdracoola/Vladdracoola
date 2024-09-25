from aiogram.filters import Filter
from aiogram import types
from aiogram.fsm.state import State, StatesGroup

api = ''


class TextFilter(Filter):
    def __init__(self, text: str):
        self.text = text

    async def __call__(self, message: types.Message) -> bool:
        return message.text == self.text


class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()
    activity = State()
