from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from loader import _


def get_menu_markup():
    builder = ReplyKeyboardBuilder()
    buttons = [
        KeyboardButton(text=_('Schedule')),
        KeyboardButton(text=_('Call schedule')),
    ]
    builder.add(*buttons)
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True)
