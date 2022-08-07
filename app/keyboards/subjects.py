from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_subjects_markup(subjects: list = None):
    markup = InlineKeyboardMarkup(row_width=2)

    buttons = [
        InlineKeyboardButton(text=s.name, callback_data=f'subjects_{s.id}') for s in subjects
    ]

    markup.add(*buttons)
    return markup
