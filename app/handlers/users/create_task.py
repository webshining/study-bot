import re
from datetime import date
from utils import logger

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType, ReplyKeyboardRemove

from app.keyboards import get_finish_markup
from app.routers import user_router as router
from app.states import CreateTaskState
from database.services import create_file, create_task
from loader import _
from .select_group import group_handler


@router.message(Command('create_task'))
async def create_task_handler(message: Message, state: FSMContext, group_id):
    if not group_id:
        return await group_handler(message=message, state=state, redirect=_get_create_task_data)
    await state.clear()
    text, markup = await _get_create_task_data(state=state)
    await message.answer(text, reply_markup=markup)


@router.message(CreateTaskState.name, lambda message: message.content_type == ContentType.TEXT)
async def create_task_name(message: Message, state: FSMContext):
    await message.answer(_("Enter text for <b>{}</b>:").format(message.text))
    await state.update_data(name=message.text)
    await state.set_state(CreateTaskState.text)


@router.message(CreateTaskState.text, lambda message: message.content_type == ContentType.TEXT)
async def create_task_text(message: Message, state: FSMContext):
    await message.answer(_("Enter task date:"))
    await state.update_data(text=message.text)
    await state.set_state(CreateTaskState.date)


@router.message(CreateTaskState.date,
                lambda message: message.content_type == ContentType.TEXT)
async def create_task_date(message: Message, state: FSMContext, group_id, user):
    match = re.match('^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$', message.text)
    if not match:
        return await message.answer(_("Invalid date format (YYYY-MM-DD)"))
    data = await state.get_data()
    task = create_task(name=data.get('name'), text=data.get('text'),
                       _date=date(year=int(match[1]), month=int(match[2]), day=int(match[3])), group_id=group_id,
                       confirmed=user.status in ("admin", "super_admin"), creator=user)
    await message.answer(_("Send files:"), reply_markup=get_finish_markup())
    await state.update_data(task_id=task.id)
    await state.set_state(CreateTaskState.files)


@router.message(CreateTaskState.files,
                lambda message: message.content_type in (ContentType.DOCUMENT, ContentType.PHOTO))
async def create_task_files(message: Message, state: FSMContext):
    if message.content_type == ContentType.DOCUMENT:
        file_id = message.document.file_id
        file_type = ContentType.DOCUMENT
    else:
        file_id = message.photo[-1].file_id
        file_type = ContentType.PHOTO

    data = await state.get_data()
    create_file(file_id, file_type, data.get('task_id'))


@router.message(CreateTaskState.files, lambda message: message.text == _("Finish"))
async def create_task_finish(message: Message, state: FSMContext):
    await message.answer(_("Success"), reply_markup=ReplyKeyboardRemove())
    await state.set_state(None)


async def _get_create_task_data(*args, **kwargs):
    state = kwargs['state']
    await state.set_state(CreateTaskState.name)
    return _("Enter task name:"), None
