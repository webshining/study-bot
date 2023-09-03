import asyncio

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.keyboards import select_markup
from app.routers import user_router as router
from database.services import update_chat
from loader import _
from utils import get_courses, get_faculties, get_groups


@router.message(Command('select_group'))
async def group_handler(message: Message):
    text = _('Select faculty:')
    await message.answer(text, reply_markup=select_markup('faculty', get_faculties(), 'name', 'id'))
    
@router.callback_query(lambda call: call.data.startswith('faculty'))
async def faculty_callback(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(_('Select course:'), reply_markup=select_markup('course', get_courses(call.data[8:]), 'name', 'id'))
    await state.update_data(faculty=call.data[8:])
    
@router.callback_query(lambda call: call.data.startswith('course'))
async def course_callback(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    faculty = data.get('faculty')
    await call.message.edit_text(_('Select group:'), reply_markup=select_markup('group', get_groups(faculty, call.data[7:]), 'name', 'id'))

@router.callback_query(lambda call: call.data.startswith('group'))
async def group_callback(call: CallbackQuery):
    if call.message.chat.type == 'group':
        if call.from_user.id in [i.user.id for i in await call.message.chat.get_administrators()]:
            update_chat(call.message.chat.id, call.data[6:])
        else:
            update_chat(call.from_user.id, call.data[6:])
    else:
        update_chat(call.from_user.id, call.data[6:])
    await call.message.edit_text(_("Success"), reply_markup=None)