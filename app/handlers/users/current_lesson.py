from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import update_markup
from app.routers import user_router as router
from loader import _, bot
from utils import get_current_time, get_timetable


@router.message(Command('current_lesson'))
async def current_lesson_handler(message: Message):
    text, markup = _get_current_lesson_data()
    await message.answer(text, reply_markup=markup)


@router.callback_query(lambda call: call.data.startswith('current'))
async def current_lesson_handler(call: CallbackQuery):
    text, markup = _get_current_lesson_data()
    await call.answer()
    try:
        if call.inline_message_id:
            return await bot.edit_message_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
        await call.message.edit_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
    except:
        pass


def _get_current_lesson_data() -> (str, any):
    timetable = get_timetable()
    now = get_current_time()
    today = [i for i in timetable if i.date == now.date()]
    lessons = [i for i in today[0].lessons if i and i.periods[0].timeEnd > now.time()] if today else None
    if lessons:
        current = lessons[0].periods[0]
        text = _('Now <b>{}</b>').format(current.disciplineFullName)
        text += _('\nEnd at <b>{}</b>').format(current.timeEnd.strftime("%H:%M")) if current.timeStart <= now.time() else _('\nStart at <b>{}</b>').format(current.timeStart.strftime("%H:%M"))
    else:
        text = _("No more lessons today")
    markup = update_markup('current')
    return text, markup