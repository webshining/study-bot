import calendar
from datetime import datetime, timedelta
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command

from app.keyboards import get_weeks_markup
from database.models import Day
from database.services import get_days
from loader import dp


@dp.message_handler(Command('schedule'))
async def schedule_handler(message: Message):
    text, markup = _get_schedule_data()
    await message.answer(text, reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data.startswith('schedule'))
async def schedule_callback_handler(call: CallbackQuery):
    if call.data[9:] == 'next':
        date = datetime.now() + timedelta(weeks=1)
    else:
        date = datetime.now()
    days = get_days(date.isocalendar().week)
    text = _get_schedule_text(days)
    try:
        await call.message.edit_text(text=text, reply_markup=get_weeks_markup('schedule', call.data[9:]))
    except:
        pass
    await call.answer()


def _get_schedule_text(days: [Day]):
    text = ''

    for index, day in enumerate(days):
        if day.subjects:
            text += f'\n\n{calendar.day_name[index]}'
            for i, subject in enumerate(day.subjects):
                text += f'\n{i + 1}) <b>{subject.name}</b>({subject.audience})'

    return text if text else 'Schedule is empty!'


def _get_schedule_data():
    date = datetime.now()
    shift = 'this'
    if date.weekday() > 4:
        shift = 'next'
        date += timedelta(weeks=1)

    days = get_days(date.isocalendar().week)
    text = _get_schedule_text(days)
    markup = get_weeks_markup('schedule', shift)
    return text, markup
