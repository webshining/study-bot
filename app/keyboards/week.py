from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_week_makrup(data: str, shift: str):
    markup = InlineKeyboardMarkup(row_width=2)

    buttons = [
        InlineKeyboardButton(text=f'This week {"*" if shift == "this" else ""}', callback_data=f'{data}_this'),
        InlineKeyboardButton(text=f'Next week {"*" if shift == "next" else ""}', callback_data=f'{data}_next')
    ]
    
    markup.add(*buttons)
    
    return markup
