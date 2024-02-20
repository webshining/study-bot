from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import _


def get_group_markup(is_admin: bool = False, state: str = None, data: any = None):
    builder = InlineKeyboardBuilder()

    if state == "subjects":
        buttons = [
            *[InlineKeyboardButton(text=i.name, callback_data=f"subjects_{i.id}") for i in data],
            InlineKeyboardButton(text=_("🔄 Refresh"), callback_data="subjects_refresh")
        ]
        if is_admin:
            buttons.append(InlineKeyboardButton(text=_("➕ Create"), callback_data="subjects_create"))
    elif state == "subject":
        buttons = []
        if is_admin:
            buttons.extend([InlineKeyboardButton(text=_("❌ Delete"), callback_data=f"subject_delete_{data}"),
                            InlineKeyboardButton(text=_("✏️ Edit"), callback_data=f"subject_edit_{data}")])
    else:
        buttons = [InlineKeyboardButton(text=_("📚 Subjects"), callback_data=f"group_subjects")]
        if is_admin:
            buttons.extend([InlineKeyboardButton(text=_("❌ Delete"), callback_data=f"group_delete")])
    builder.add(*buttons)
    builder.adjust(2)

    return builder.as_markup()
