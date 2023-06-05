from aiogram.filters import Command
from aiogram.types import Message

from loader import _, dp
from utils import Call, get_timetable_call


@dp.message(Command('call_schedule'))
async def call_schedule_handler(message: Message):
    text = _get_call_schedule_data()
    await message.answer(text)


def _get_call_schedule_data() -> str:
    return _get_call_schedule_text(get_timetable_call())


def _get_call_schedule_text(calls: list[Call]) -> str:
    text = ''
    for i, v in enumerate(calls):
        text += f'\n{i+1})\t {v.timeStart.strftime("%H:%M")} - {v.timeEnd.strftime("%H:%M")}'
    return text or "Call timetable is empty!"