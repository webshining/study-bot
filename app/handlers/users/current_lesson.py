from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.keyboards import get_update_markup
from app.routers import user_router as router
from loader import _, bot
from utils import get_current_time, get_schedule
from .select_group import group_handler


@router.message(Command('current_lesson'))
async def current_lesson_handler(message: Message, group_id, state: FSMContext):
    if not group_id:
        return await group_handler(message, state, _get_current_lesson_data)
    text, markup = await _get_current_lesson_data(group_id)
    await message.answer(text, reply_markup=markup)


@router.callback_query(lambda call: call.data.startswith('current'))
async def current_lesson_callback(call: CallbackQuery, group_id):
    if not group_id:
        return await call.answer(_("You haven't selected a group yet🫡"))
    await call.answer(str(get_current_time().date()))
    text, markup = await _get_current_lesson_data(group_id)
    try:
        if call.inline_message_id:
            return await bot.edit_message_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
        await call.message.edit_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
    except:
        pass


async def _get_current_lesson_data(group_id: int, *args, **kwargs) -> (str, any):
    timetable = get_schedule(group_id)
    text = _("It seems the servers are not responding, and there is no saved data for you🫡")
    if timetable:
        now = get_current_time()
        today = [i for i in timetable if i.date == now.date()]
        lessons = [i for i in today[0].lessons if i and i.periods[0].timeEnd.time() > now.time()] if today else None
        if lessons:
            current = lessons[0].periods[0]
            text = _('Now <b>{}</b>').format(current.disciplineFullName)
            text += _('\nEnd in <b>{}</b>').format(
                str(current.timeEnd - now).split(".")[0]) if current.timeStart.time() <= now.time() else _(
                '\nStart in <b>{}</b>').format(str(current.timeStart - now).split(".")[0])
        else:
            text = _("No more lessons today🫡")
    markup = get_update_markup('current')
    return text, markup
