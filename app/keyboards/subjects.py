from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_subjects_keyboard(subjects: list):
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(text=s.name, callback_data=f'subjects_{s.id}') for s in subjects
    ]
    markup.add(*buttons)
    return markup
