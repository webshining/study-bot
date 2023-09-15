from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from loader import _


def get_finish_markup():
    builder = ReplyKeyboardBuilder()
    buttons = [
        KeyboardButton(text=_('Finish'))
    ]
    builder.add(*buttons)
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True)
