import datetime, calendar
from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from loader import dp
from database import get_week


@dp.message_handler(Command('schedule'))
async def schedule_handler(message: Message):
    text = _get_subjects_text(get_week(datetime.datetime.now().isocalendar()[1]))
    await message.answer(text)


def _get_subjects_text(week: list):
    text = ''
    for index, day in enumerate(week):
        if day.subjects:
            week_day = calendar.day_name[index]
            text += f'{week_day}:\n'
            for i, subject in enumerate(day.subjects):
                text += f'{i+1}) <b>{subject.name}({subject.audience})</b>\n\n'

    return text if text != '' else 'Schedule is empty'
