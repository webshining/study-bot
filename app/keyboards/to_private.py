from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_to_private_makrup():
    builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Go to private', url="https://t.me/fit_3_bot"),
    ]
    builder.add(*buttons)
    builder.adjust(3)
    return builder.as_markup()
