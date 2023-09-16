from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from app.routers import admin_router as router
from database.services import get_tasks, get_task
from app.keyboards import get_select_markup
from loader import _


@router.message(Command('confirm_tasks'))
async def confirm_tasks_handler(message: Message, group_id, user):
    text, markup = _get_confirm_tasks_data(group_id=group_id if user.status == 'admin' else None)
    await message.answer(text, reply_markup=markup)


@router.callback_query(lambda call: call.data.startswith('confirm_tasks'))
async def confirm_tasks_callback(call: CallbackQuery):
    task = get_task(call.data[14:])
    task.confirmed = True
    task.save()
    text, markup = _get_confirm_tasks_data()
    await call.message.edit_text(text, reply_markup=markup)


async def _get_confirm_tasks_data(group_id: int = None, *args, **kwargs):
    tasks = list(filter(lambda i: i.status != 'task', get_tasks(group_id=group_id)))
    if not tasks:
        text = _("Tasks is empty🫡")
    else:
        text = _get_confirm_tasks_text(tasks)
    markup = get_select_markup('confirm_tasks', [{'id': t.id, 'text': i + 1} for i, t in enumerate(tasks)])
    return text, markup


def _get_confirm_tasks_text(tasks: list) -> str:
    text = ''
    for i, task in enumerate(tasks):
        text += f'\n{i + 1}) <b>{task.name}</b>\n{task.text}'
    return text
