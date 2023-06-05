from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import update_markup
from loader import _, dp
from utils import current_time, get_timetable


@dp.message(Command('current_lesson'))
async def current_lesson_handler(message: Message):
    text, markup = _get_current_lesson_data()
    await message.answer(text, reply_markup=markup)


@dp.callback_query(lambda call: call.data.startswith('current'))
async def current_lesson_handler(call: CallbackQuery):
    text, markup = _get_current_lesson_data()
    try:
        await call.message.edit_text(text, reply_markup=markup)
    except:
        pass
    await call.answer()


def _get_current_lesson_data() -> str:
    timetable = get_timetable()
    now = current_time()
    today = [i for i in timetable if i.date == now.date()]
    lessons = [i for i in today[0].lessons if i and i.periods[0].timeEnd > now.time()] if today else None
    if lessons:
        current = lessons[0].periods[0]
        text = f'Now <b>{current.disciplineFullName}</b>'
        text += f'\nEnd at <b>{current.timeEnd.strftime("%H:%M")}</b>' if current.timeStart <= now.time() else f'\nStart at <b>{current.timeStart.strftime("%H:%M")}</b>'
    else:
        text = "No more lessons today"
    markup = update_markup('current')
    return text, markup