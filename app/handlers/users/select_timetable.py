from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from loader import dp, _
from app.keyboards import select_markup
from utils import get_faculties, get_courses, get_groups
from database.services import create_or_update_chat


@dp.message(Command('select_timetable'))
async def _select_timetable(message: Message):
    await message.answer(_("Select faculty:"), reply_markup=select_markup('faculty', get_faculties(), "fullName", "id"))


@dp.callback_query(lambda call: call.data.startswith('faculty'))
async def _select_faculty(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(_("Select course:"), reply_markup=select_markup('course', get_courses(call.data[8:]), "course", "course"))
    await state.update_data(facultyId=call.data[8:])
    await call.answer()


@dp.callback_query(lambda call: call.data.startswith('course'))
async def _select_course(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if data.get('facultyId'):
        await call.message.edit_text(_("Select group:"), reply_markup=select_markup('group', get_groups(data.get('facultyId'), call.data[7:]), "name", "id"))
        await state.update_data(courseId=call.data[7:])
    else:
        await call.message.edit_text(_("Looks like your previous replies have been reset.\nSelect faculty:"), reply_markup=select_markup('faculty', get_faculties(), 'fullName', 'id'))
        await state.clear()
    await call.answer()


@dp.callback_query(lambda call: call.data.startswith('group'))
async def _select_group(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if data.get('facultyId') and data.get('courseId'):
        create_or_update_chat(call.message.chat.id, data.get('facultyId'), data.get('courseId'), call.data[6:])
        await call.message.edit_text(_("Successfully!"), reply_markup=None)
    else:
        await call.message.edit_text(_("Looks like your previous replies have been reset.\nSelect faculty:"), reply_markup=select_markup('faculty', get_faculties(), 'fullName', 'id'))
        await call.answer()
    await state.clear()
