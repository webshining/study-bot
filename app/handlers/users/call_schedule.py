from aiogram.filters import Command
from aiogram.types import Message

from app.routers import user_router as router
from loader import _
from utils import Call, get_timetable_call


@router.message(Command('call_schedule'))
@router.message(lambda message: message.text == _('Call schedule 🔔'))
async def call_schedule_handler(message: Message):
    text = _get_call_schedule_data()
    await message.answer(text)


def _get_call_schedule_data() -> str:
    timetable_call = get_timetable_call()
    if not timetable_call:
        return _("It seems the servers are not responding, and there is no saved data for you🫡")
    return _get_call_schedule_text(timetable_call)


def _get_call_schedule_text(calls: list[Call]) -> str:
    text = ''
    for i, v in enumerate(calls):
        text += f'\n{i + 1})\t {v.timeStart.strftime("%H:%M")} - {v.timeEnd.strftime("%H:%M")}'
    return text or _("Call schedule is empty🫡")
