from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import _


def get_update_markup(data: str, *buttons: InlineKeyboardButton):
    builder = InlineKeyboardBuilder()
    _buttons = [
        InlineKeyboardButton(text=_('🔄Update'), callback_data=data),
        *buttons
    ]
    builder.add(*_buttons)
    builder.adjust(2)
    return builder.as_markup()
