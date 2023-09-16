from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from loader import _


def get_menu_markup():
    builder = ReplyKeyboardBuilder()
    buttons = [
        KeyboardButton(text=_('Schedule 📖')),
        KeyboardButton(text=_('Call schedule 🔔')),
        KeyboardButton(text=_('Current lesson 🔎')),
        KeyboardButton(text=_('Select Group 👥')),
    ]
    builder.add(*buttons)
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)
