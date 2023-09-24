from datetime import timedelta

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.keyboards import get_week_markup
from app.routers import user_router as router
from database.services import get_tasks
from loader import _, bot
from utils import get_current_time, week_start_end

from .select_group import group_handler


@router.message(Command('tasks'))
async def tasks_handler(message: Message, group_id, state: FSMContext):
    if not group_id:
        return await group_handler(message, state, _get_tasks_data)
    text, markup = await _get_tasks_data(group_id)
    await message.answer(text, reply_markup=markup)


@router.callback_query(lambda call: call.data.startswith('tasks'))
async def tasks_callback(call: CallbackQuery, group_id):
    if not group_id:
        return await call.answer(_("You haven't selected a group yet🫡"))
    text, markup = await _get_tasks_data(group_id, call.data[6:])
    try:
        if call.inline_message_id:
            return await bot.edit_message_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
        await call.message.edit_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
    except:
        pass
    await call.answer()


async def _get_tasks_data(group_id, shift: str = "this", *args, **kwargs) -> (str, any):
    date = get_current_time()
    if shift == 'next':
        date += timedelta(weeks=1)
    tasks = get_tasks(group_id, week_start_end(date), status='task')
    if not tasks:
        text = _("Tasks is empty🫡")
    else:
        text = _get_tasks_text(tasks)
    markup = get_week_markup('tasks', shift)
    return text, markup


def _get_tasks_text(tasks: list) -> str:
    weekdays = _('Monday Tuesday Wednesday Thursday Friday Saturday Sunday').split(" ")
    
    text = []
    i = 1
    
    for task in tasks:
        t = f"\n\n{weekdays[task.date.weekday()]}"
        if t in text:
            i += 1
        else:
            i = 1
            text.append(t)
        text.append(f"\n{i}) <b>{task.name}</b>\n{task.text}")
    
    return "".join(text)
