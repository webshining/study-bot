from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_update_makrup(data: str):
    markup = InlineKeyboardMarkup(row_width=2)

    buttons = [
        InlineKeyboardButton(text='Update', callback_data=f'{data}_update'),
    ]
    
    markup.add(*buttons)
    
    return markup
