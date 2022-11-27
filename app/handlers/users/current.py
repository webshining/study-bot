from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from loader import dp, bot, _
from database.services import get_day_by_date
from app.keyboards import get_update_markup
from .subjects import _get_subject_text
from utils import current_time


@dp.message(Command('current'))
async def current_handler(message: Message):
    text, markup = _get_current_data()
    await message.answer(text, reply_markup=markup)


@dp.callback_query(lambda call: call.data.startswith('current_update'))
async def current_callback_handler(call: CallbackQuery):
    await call.answer()
    text, markup = _get_current_data()
    try:
        if call.inline_message_id:
            await bot.edit_message_text(text=text, inline_message_id=call.inline_message_id, reply_markup=markup)
        else:
            await bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)
    except:
        pass


def _get_current_data():
    _current_time = current_time()
    day = get_day_by_date(_current_time)
    subjects = day.subjects
    if not subjects:
        text = _('No class today')
    else:
        subjects = [s for s in subjects if s.time_end >= _current_time.time()]
        if not subjects:
            text = _('Classes are over')
        elif _current_time >= subjects[0].time_start:
            text = _get_subject_text(subjects[0].subject)
            text += _('\n\nСlass ends at {} in {}').format(subjects[0].time_end, subjects[0].time_end - _current_time)
        else:
            text = _('No class right now! Next class: {} at {} in {}').format(subjects[0].subject.name, subjects[0].time_start, subjects[0].time_start - _current_time)
    
    markup = get_update_markup('current_update')
    return text, markup.as_markup()
