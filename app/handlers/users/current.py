from datetime import datetime

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command

from loader import dp, bot
from database.services import get_day_by_date
from app.keyboards import get_update_makrup
from .subjects import _get_subject_text
from utils import current_time, str_to_time


@dp.message_handler(Command('current'))
async def current_handler(message: Message):
    text, markup = _get_current_data()
    await message.answer(text, reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data.startswith('current'))
async def current_callback_handler(call: CallbackQuery):
    await call.answer()
    text, markup = _get_current_data()
    try:
        if call.inline_message_id:
            await bot.edit_message_text(text, message_id=call.inline_message_id,
                                        inline_message_id=call.inline_message_id, reply_markup=markup)
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
    print(str_to_time('00:20:00', _format) - str_to_time('10:20:00', _format))
    if not subject_now:
        text = f'Classes are over!'
    elif _current_time >= subject_now[0].time_start:
        text = _get_subject_text(subject_now[0].subject)
        text += f'\n\nСlass ends at {subject_now[0].time_end} in {str_to_time(subject_now[0].time_end, _format) - str_to_time(_current_time, _format)}'
    else:
        text = f'No class right now! Next class: {subject_now[0].subject.name}'

    markup = get_update_makrup('current')
    return text, markup
