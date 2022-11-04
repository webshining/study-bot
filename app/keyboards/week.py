from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_week_makrup(data: str, shift: str):
    builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text=f'This week {"*" if shift == "this" else ""}', callback_data=f'{data}_this'),
        InlineKeyboardButton(text=f'Next week {"*" if shift == "next" else ""}', callback_data=f'{data}_next')
    ]
    builder.add(*buttons)
    builder.adjust(3)
    return builder.as_markup()
