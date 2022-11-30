from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import _
from database import List


def lists_markup(data: str, lists: list[List]):
    builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text=lst.name, callback_data=f'{data}_{lst.id}') for lst in lists
    ]
    builder.add(*buttons)
    builder.adjust(2)
    return builder


def list_markup(lst: List, is_admin: bool = False):
    builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text=_("➕Write"), callback_data=f'list_write_{lst.id}'),
        InlineKeyboardButton(text=_('🔄Update'), callback_data=f'list_update_{lst.id}'),
        InlineKeyboardButton(text=_('⬅️Back'), callback_data=f'list_back'),
    ]
    if is_admin:
        buttons = [
            InlineKeyboardButton(text=_('Turn off') if lst.visible else _("Turn on"), callback_data=f'list_turn_{lst.id}'),
            InlineKeyboardButton(text=_('✏️Rename'), callback_data=f'list_rename_{lst.id}'),
            InlineKeyboardButton(text=_('❌Delete'), callback_data=f'list_delete_{lst.id}'),
            *buttons
        ]
    builder.add(*buttons)
    builder.adjust(3)
    return builder

