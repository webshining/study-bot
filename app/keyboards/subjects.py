from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.models import Subject


def get_subjects_makrup(data: str, subjects: list[Subject]):
    markup = InlineKeyboardMarkup(row_width=2)

    buttons = [
        InlineKeyboardButton(text=subject.name, callback_data=f'{data}_{subject.id}') for subject in subjects
    ]
    
    markup.add(*buttons)
    
    return markup


def get_back_markup(data: str):
    markup = InlineKeyboardMarkup(row_width=2)

    buttons = [
        InlineKeyboardButton(text=f'⬅️Back', callback_data=f'{data}_back')
    ]
    
    markup.add(*buttons)
    
    return markup
