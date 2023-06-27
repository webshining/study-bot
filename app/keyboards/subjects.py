from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.models import Subject


def subjects_markup(data: str, subjects: list[Subject]):
    builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text=subject.name, callback_data=f'{data}_{subject.id}') for subject in subjects
    ]
    builder.add(*buttons)
    builder.adjust(3)
    return builder.as_markup()
