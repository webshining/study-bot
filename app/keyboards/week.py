from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_week_keyboard(data: str, week: str = 'this'):
    markup = InlineKeyboardMarkup(row_width=2)

    buttons = [
        InlineKeyboardButton(text='This week' if week == 'next' else 'This week*', callback_data=f'{data}_this'),
        InlineKeyboardButton(text='Next week' if week == 'this' else 'Next week*', callback_data=f'{data}_next')
    ]
    markup.add(*buttons)

    return markup
