from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_week_markup(data: str, shift: str = 'this'):
    markup = InlineKeyboardMarkup(row_width=2)

    buttons = [
        InlineKeyboardButton(text=f'This week {"*" if shift == "this" else ""}', callback_data=f'{data}_this'),
        InlineKeyboardButton(text=f'Next week {"*" if shift == "next" else ""}', callback_data=f'{data}_next')
    ]
    markup.add(*buttons)

    return markup
