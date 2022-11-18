from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from loader import dp, bot
from database.services import get_day_by_date
from app.keyboards import get_update_markup
from .subjects import _get_subject_text
from utils import current_time, str_to_time


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
    _format: str = '%H:%M:%S'
    _current_time = current_time()
    day = get_day_by_date(_current_time)
    _current_time = _current_time.time().strftime(_format)
    subject_now = [s for s in day.subjects if s.time_end >= _current_time]
    if not subject_now:
        text = f'Classes are over!'
    elif _current_time >= subject_now[0].time_start:
        text = _get_subject_text(subject_now[0].subject)
        text += f'\n\nСlass ends at {subject_now[0].time_end} in {str_to_time(subject_now[0].time_end, _format) - str_to_time(_current_time, _format)}'
    else:
        text = f'No class right now! Next class: {subject_now[0].subject.name} at {subject_now[0].time_start} in {str_to_time(subject_now[0].time_start, _format) - str_to_time(_current_time, _format)}'

    markup = get_update_markup('current_update')
    return text, markup
