from aiogram.filters import Command
from aiogram.types import Message

from app.routers import admin_router as router
from database.services import get_tasks
from app.keyboards import get_select_markup
from loader import _


@router.message(Command('confirm_tasks'))
async def confirm_tasks_handler(message: Message):
    text, markup = _get_confirm_tasks_data()
    await message.answer(text, reply_markup=markup)


def _get_confirm_tasks_data():
    tasks = get_tasks(confirmed=False)
    if not tasks:
        text = _("Tasks is empty🫡")
    else:
        text = _get_confirm_tasks_text(tasks)
    markup = get_select_markup('confirm_tasks', [{'id': t.id, 'name': i + 1} for i, t in enumerate(tasks)])
    return text, markup


def _get_confirm_tasks_text(tasks: list) -> str:
    text = ''
    for i, task in enumerate(tasks):
        text += f'\n{i + 1}) <b>{task.name}</b>\n{task.text}'
    return text
