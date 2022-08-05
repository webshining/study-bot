from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from loader import dp, _, bot
from database import get_subjects, get_subject


def _get_subject_text(subject):
    text = ''
    text += _('<b>{}</b>\n\n'
              'Audience: <b>{}</b>\n'
              'Teacher: <b>{}</b>\n\n'
              '{}').format(subject.name, subject.audience, subject.teacher, subject.info)
    if subject.files:
        text += _('\n\bFiles:')
    return text
