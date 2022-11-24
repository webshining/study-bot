from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.models import List


def get_lists_markup(data: str, lists: list[List]):
    builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text=list.name, callback_data=f'{data}_{list.id}') for list in lists
    ]
    builder.add(*buttons)
    builder.adjust(3)
    return builder.as_markup()
