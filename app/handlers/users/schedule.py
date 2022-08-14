import calendar
from datetime import datetime, timedelta
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from app.keyboards import get_week_keyboard
from loader import dp
from database import get_week_subjects, Subject


@dp.message_handler(Command('schedule'))
async def schedule_handler(message: Message):
    text, markup = _get_schedule_data()
    await message.answer(text, reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data.startswith('schedule'))
async def schedule_call_back_handler(call: CallbackQuery):
    if call.data[9:] == 'this':
        week = datetime.today().isocalendar().week
    else:
        week = datetime.today().isocalendar().week + 1
    markup = get_week_keyboard('schedule', call.data[9:])
    text = _get_schedule_text(get_week_subjects(week))
    try:
        await call.message.edit_text(text, reply_markup=markup)
    except Exception as e:
        await call.answer('Nothing has changed!', show_alert=True)


def _get_schedule_data():
    week = 'this'
    now = datetime.today()
    if now.weekday() >= 4 and now.hour >= 13:
        week = 'next'
        now += timedelta(weeks=1)

    text = _get_schedule_text(get_week_subjects(now.isocalendar().week))
    markup = get_week_keyboard('schedule', week)
    return text, markup


def _get_schedule_text(days: list[list[Subject]]):
    text = ''
    for index, day in enumerate(days):
        if day:
            text += f'\n\n{calendar.day_name[index]}:'
            for i, subject in enumerate(day):
                        text += f'\n{i+1}) <b>{subject.name}</b>({subject.audience})'
    return text if text != '' else 'Schedule is empty!'
