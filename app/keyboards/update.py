from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import _


def get_update_markup(data: str):
    builder = InlineKeyboardBuilder()
    _buttons = [
        InlineKeyboardButton(text=_('🔄 Update'), callback_data=f'{data}_update'),
    ]
    builder.add(*_buttons)
    builder.adjust(1)
    return builder.as_markup()
