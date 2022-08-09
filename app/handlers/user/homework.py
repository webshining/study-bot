import calendar
from datetime import datetime, timedelta
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from loader import _, dp
from database import get_week_tasks, Task
from app.keyboards import get_week_markup


@dp.message_handler(Command('homework'))
async def homework_handler(message: Message):
    text, markup = _get_homework_data()
    await message.answer(text, reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data.startswith('homework'))
async def schedule_week_handler(call: CallbackQuery):
    if call.data[9:] == 'this':
        date = datetime.now()
    elif call.data[9:] == 'next':
        date = datetime.now() + timedelta(weeks=1)
    text = _get_homework_text(get_week_tasks(date.isocalendar().week))
    try:
        await call.message.edit_text(text=text, reply_markup=get_week_markup('homework', call.data[9:]))
    except Exception as e:
        await call.answer(_('Nothing changed'), show_alert=True)


def _get_homework_text(week: list[list[Task]]):
    text = ''
    for index, day in enumerate(week):
        if day:
            text += f'\n\n{calendar.day_name[index]}'
            for i, task in enumerate(day):
                text += f'\n{i+1}) <b>{task.subject.name}:</b>\n{task.text}'

    return text if text != '' else _('Homework is empty')


def _get_homework_data():
    shift = 'this'
    now = datetime.now()
    if now.weekday() > 4 and now.hour > 13:
        shift = 'next'
        now += timedelta(weeks=1)

    text = _get_homework_text(get_week_tasks(now.isocalendar().week))
    markup = get_week_markup('homework', shift)

    return text, markup
