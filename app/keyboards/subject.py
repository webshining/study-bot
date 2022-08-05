from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _


def get_subject_keyboard(subject, delete: bool = False):
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(text=_('back'), callback_data='subject_back')]
    if subject.files:
        buttons.append(*[InlineKeyboardButton(text=f.name, callback_data=f'file_{f.file_id}') for f in subject.files])
    if delete:
        buttons.append(InlineKeyboardButton(text=_('delete'), callback_data=f'subject_{subject.id}'))
    markup.add(*buttons)
    return markup
