import calendar
from datetime import datetime, timedelta
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command
from loader import dp
from app.keyboards import get_week_markup
from database import get_tasks_by_week, Task


@dp.message_handler(Command('homework'))
async def homework_andler(message: Message):
    text, markup = await _get_homework_data()
    await message.answer(text, reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data.startswith('homework'))
async def homework_callback_handler(call: CallbackQuery):
    if call.data[9:] == 'this':
        _date = datetime.now()
    else:
        _date = datetime.now() + timedelta(weeks=1)
    days = await get_tasks_by_week(_date.isocalendar().week)
    text = _get_homework_text(days)
    try:
        await call.message.edit_text(text, reply_markup=get_week_markup('homework', call.data[9:]))
    except:
        await call.answer('Nothing changed!')
    await call.answer()


def _get_homework_text(days: list[list[Task]]):
    text = ''
    for index, day in enumerate(days):
        if day:
            text += f'{calendar.day_name[index]}'
            for task in day:
                text += f'<b>{task.subject.name}:</b>\n{task.text}'

    return text if text != '' else "Homework is empty!"


async def _get_homework_data():
    current_date = datetime.now()
    days = await get_tasks_by_week(current_date.isocalendar().week)
    shift = 'this'
    if current_date.weekday() > 4:
        shift = 'next'
    text = _get_homework_text(days)
    markup = get_week_markup('homework', shift)
    return text, markup
