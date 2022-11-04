from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_update_makrup(data: str):
    builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='🔄Update', callback_data=f'{data}_update'),
    ]
    builder.add(*buttons)
    builder.adjust(3)
    return builder.as_markup()
