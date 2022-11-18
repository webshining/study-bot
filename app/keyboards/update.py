from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_update_markup(data: str, value: str = None):
    builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='🔄Update', callback_data=f'{data}{f"_{value}" if value else ""}'),
    ]
    builder.add(*buttons)
    builder.adjust(3)
    return builder.as_markup()
