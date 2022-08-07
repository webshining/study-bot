import calendar

from datetime import datetime, timedelta
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from loader import dp, bot, _
from database import get_week
from app.keyboards import get_week_markup


@dp.message_handler(Command('schedule'))
async def schedule_handler(message: Message):
    text, markup = _get_schedule_data()
    await message.answer(text, reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data.startswith('schedule'))
async def schedule_week_handler(call: CallbackQuery):
    global date
    if call.data[9:] == 'this':
        date = datetime.now()
    elif call.data[9:] == 'next':
        date = datetime.now() + timedelta(weeks=1)

    week_schedule = get_week(date.isocalendar()[1])
    text = _get_schedule_text(week_schedule)
    try:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=text, reply_markup=get_week_markup('schedule', call.data[9:]))

    except Exception as e:
        await call.answer(_('Nothing changed'), show_alert=True)


def _get_schedule_text(week: list):
    text = ''
    for index, day in enumerate(week):
        if day.subjects:
            week_day = calendar.day_name[index]
            text += f'{week_day}:\n'
            for i, subject in enumerate(day.subjects):
                text += f'{i + 1}) <b>{subject.name}({subject.audience})</b>\n\n'

    return text if text != '' else 'Schedule is empty'


def _get_schedule_data():
    shift = 'this'
    now = datetime.now()
    if now.weekday() > 4 or (now.weekday() == 4 and now.hour > 13):
        shift = 'next'
        now += timedelta(weeks=1)

    week_schedule = get_week(now.isocalendar()[1])

    text = _get_schedule_text(week_schedule)

    markup = get_week_markup('schedule', shift)
    return text, markup
