from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup

from loader import dp, _
from database import get_subjects, add_task
from app.keyboards import get_subjects_markup


class Task(StatesGroup):
    text = State()


@dp.message_handler(Command('add_task'))
async def add_task_handler(message: Message):
    await message.answer(_('Select subject:'), reply_markup=get_subjects_markup('tasks', get_subjects()))


@dp.callback_query_handler(lambda call: call.data.startswith('tasks'))
async def add_task_subject_handler(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text=_('Send text:'), reply_markup=None)
    await state.update_data(subject=int(call.data[6:]))
    await Task.text.set()


@dp.message_handler(content_types=['text'], state=Task.text)
async def add_task_text_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    add_task(message.text, data.get('subject'))
    await message.answer(_('Task added'))
    await state.finish()
