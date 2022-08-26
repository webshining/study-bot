import calendar
from datetime import datetime, timedelta
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command
from loader import dp
from database import get_days, Day
from app.keyboards import get_week_markup


@dp.message_handler(Command('schedule'))
async def schedule_handler(message: Message):
    text, markup = await _get_schedule_data()
    await message.answer(text, reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data.startswith('schedule'))
async def schedule_callback_handler(call: CallbackQuery):
    current_date = datetime.now()
    current_date += timedelta(weeks=(1 if call.data[9:] == 'next' else 0))
    text = _get_schedule_text(await get_days(current_date.isocalendar().week))
    markup = get_week_markup('schedule', call.data[9:])
    try:
        await call.message.edit_text(text, reply_markup=markup)
    except:
        await call.answer('Nothing changed', show_alert=True)
    await call.answer()


def _get_schedule_text(days: list[Day]):
    text = ''
    for index, day in enumerate(days):
        if day.subjects:
            text += f'\n\n{calendar.day_name[index]}'
            for i, subject in enumerate(day.subjects):
                text += f'\n{i + 1}) <b>{subject.name}</b>({subject.audience})'

    return text if text != '' else 'Schedule is empty'


async def _get_schedule_data():
    shift = 'this'
    current_date = datetime.now()
    if datetime.now().weekday() > 4:
        shift = 'next'
        current_date += timedelta(weeks=1)

    text = _get_schedule_text(await get_days(current_date.isocalendar().week))
    markup = get_week_markup('schedule', shift)
    return text, markup
