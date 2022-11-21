import calendar
from datetime import timedelta
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from loader import dp, bot
from database.models import Day
from database.services import get_days
from app.keyboards import get_week_makrup
from utils import current_time


@dp.message(Command('schedule'))
async def schedule_handler(message: Message):
    text, markup = _get_schedule_data()
    await message.answer(text=text, reply_markup=markup)


@dp.callback_query(lambda call: call.data.startswith('schedule'))
async def schedule_callback_handler(call: CallbackQuery):
    await call.answer()
    date = current_time()
    if call.data[9:] == 'next':
        date += timedelta(weeks=1)
    days = get_days(date.isocalendar().week)
    text = _get_schedule_text(days)
    markup = get_week_makrup('schedule', call.data[9:])
    try:
        if call.inline_message_id:
            await bot.edit_message_text(text=text, inline_message_id=call.inline_message_id, reply_markup=markup)
        else:
            await bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)
    except:
        pass


def _get_schedule_text(days):
    text = ''
    if days:
        for day in days:
            if day.subjects:
                text += f'\n\n{calendar.day_name[day.day_id]}'
                for si, subject in enumerate(day.subjects):
                    text += f'\n{si + 1}) <b>{subject.subject.name}</b>({subject.subject.audience})'
    return text if text else 'Schedule is empty🫡'


def _get_schedule_data():
    shift = 'this'
    _current_time = current_time()
    if _current_time.weekday() >= 5:
        _current_time += timedelta(weeks=1)
        shift = 'next'

    text = _get_schedule_text(get_days(_current_time.isocalendar().week))
    markup = get_week_makrup('schedule', shift)
    return text, markup
