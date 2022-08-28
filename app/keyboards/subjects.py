from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_subjects_markup(data: str, subjects: list):
    markup = InlineKeyboardMarkup(row_width=2)

    buttons = [
        InlineKeyboardButton(text=subject.name, callback_data=f'{data}_{subject.id}') for subject in subjects
    ]
    markup.add(*buttons)

    return markup
