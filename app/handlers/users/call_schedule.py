from aiogram.filters import Command
from aiogram.types import Message

from app.routers import user_router as router
from loader import _
from utils import Call, get_timetable_call


@router.message(Command('call_schedule'))
async def call_schedule_handler(message: Message):
    text = _get_call_schedule_data()
    await message.answer(text)


def _get_call_schedule_data() -> str:
    return _get_call_schedule_text(get_timetable_call())


def _get_call_schedule_text(calls: list[Call]) -> str:
    text = ''
    for i, v in enumerate(calls):
        text += f'\n{i+1})\t {v.timeStart.strftime("%H:%M")} - {v.timeEnd.strftime("%H:%M")}'
    return text or _("Call schedule is empty🫡")