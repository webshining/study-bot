from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_select_markup(data: str, lst: list[object], key_text: str = 'text', key_data: str = 'id'):
    builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text=str(i[key_text]), callback_data=f'{data}_{str(i[key_data])}') for i in map(dict, lst)
    ]
    builder.add(*buttons)
    builder.adjust(2)
    return builder.as_markup()
