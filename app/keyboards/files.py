from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_files_markup(data: str, files: list):
    markup = InlineKeyboardMarkup(row_width=2)

    buttons = [
        InlineKeyboardButton(text=file.name, callback_data=f'{data}_{file.id}') for file in files
    ]
    markup.add(*buttons)
    return markup
