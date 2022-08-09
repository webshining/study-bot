import calendar

from datetime import datetime, timedelta
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from loader import dp, _
from database import get_week_subjects, Subject
from app.keyboards import get_week_markup


@dp.message_handler(Command('schedule'))
async def schedule_handler(message: Message):
    text, markup = _get_schedule_data()
    await message.answer(text, reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data.startswith('schedule'))
async def schedule_week_handler(call: CallbackQuery):
    if call.data[9:] == 'this':
        date = datetime.now()
    elif call.data[9:] == 'next':
        date = datetime.now() + timedelta(weeks=1)
    text = _get_schedule_text(get_week_subjects(date.isocalendar().week))
    try:
        await call.message.edit_text(text=text, reply_markup=get_week_markup('schedule', call.data[9:]))
    except Exception as e:
        await call.answer(_('Nothing changed'), show_alert=True)


def _get_schedule_text(week: list[list[Subject]]):
    text = ''
    for index, day in enumerate(week):
        if day:
            text += f'\n\n{calendar.day_name[index]}'
            for i, subject in enumerate(day):
                text += f'\n{i + 1}) <b>{subject.name}</b>({subject.audience})'

    return text if text != '' else _('Schedule is empty')


def _get_schedule_data():
    shift = 'this'
    now = datetime.now()
    if now.weekday() > 4 and now.hour > 13:
        shift = 'next'
        now += timedelta(weeks=1)

    text = _get_schedule_text(get_week_subjects(now.isocalendar().week))
    markup = get_week_markup('schedule', shift)

    return text, markup
