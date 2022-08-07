from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _


def get_week_markup(data: str, shift: str = 'this'):
    markup = InlineKeyboardMarkup(row_width=1)
    this_week_text = _('На эту неделю') + ('*' if shift == 'this' else '')
    next_week_text = _('На следущую неделю') + ('*' if shift == 'next' else '')
    buttons = [
        InlineKeyboardButton(this_week_text, callback_data=f'{data}_this'),
        InlineKeyboardButton(next_week_text, callback_data=f'{data}_next'),
    ]
    markup.add(*buttons)
    return markup
