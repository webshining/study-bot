from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_update_markup(data: str):
    builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='🔄Update', callback_data=f'{data}'),
    ]
    builder.add(*buttons)
    builder.adjust(3)
    return builder