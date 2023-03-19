from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def select_markup(data: str, lst: list[object], key_text: any, key_data: any):
    builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text=i[key_text], callback_data=f'{data}_{i[key_data]}') for i in map(dict, lst)
    ]
    builder.add(*buttons)
    builder.adjust(2)
    return builder.as_markup()
