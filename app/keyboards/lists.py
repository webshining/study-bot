from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import _
from database.models import List


def lists_markup(data: str, lists: list[List]):
    builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text=list.name, callback_data=f'{data}_{list.id}') for list in lists
    ]
    builder.add(*buttons)
    builder.adjust(3)
    return builder


def list_markup(list: List, is_admin: bool = False):
    builder = InlineKeyboardBuilder()
    builder.row()
    if is_admin:
        builder.add(InlineKeyboardButton(text=_("Turn off") if list.visible else _("Turn on"),
                                         callback_data=f'list_visible_{list.id}'),
                    InlineKeyboardButton(text=_("✏️Edit name"), callback_data=f'list_edit_{list.id}'),
                    InlineKeyboardButton(text=_("❌Remove"), callback_data=f'list_remove_{list.id}'))
        builder.adjust(3)
    builder.row(InlineKeyboardButton(text=_('➕Write'), callback_data=f'list_write_{list.id}'))
    builder.row(InlineKeyboardButton(text=_('🔄Update'), callback_data=f'list_update_{list.id}'))
    builder.row(InlineKeyboardButton(text=_("⬅️Back"), callback_data=f'list_back'))
    return builder
