from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import _


def get_week_markup(data: str, shift: str):
    builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text=_('This week') + ('*' if shift == 'this' else ''), callback_data=f'{data}_this'),
        InlineKeyboardButton(text=_('Next week') + ('*' if shift == 'next' else ''), callback_data=f'{data}_next')
    ]
    builder.add(*buttons)
    builder.adjust(3)
    return builder.as_markup()
