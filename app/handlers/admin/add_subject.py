from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp, _, bot
from database import add_subject


class AddSubject(StatesGroup):
    name = State()
    audience = State()
    teacher = State()
    info = State()


@dp.message_handler(Command('add_subject'))
async def add_subject_handler(message: Message, state: FSMContext):
    message = await message.answer(_('Subject name:'))
    await state.update_data(message_id=message.message_id)
    await AddSubject.name.set()


@dp.message_handler(content_types=['text'], state=AddSubject.name)
async def add_subject_name(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.update_data(name=message.text)
    await message.delete()
    await bot.edit_message_text(chat_id=message.chat.id, message_id=data.get('message_id'), text=_('Subject audience:'))
    await AddSubject.audience.set()


@dp.message_handler(content_types=['text'], state=AddSubject.audience)
async def add_subject_audience(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.update_data(audience=message.text)
    await message.delete()
    await bot.edit_message_text(chat_id=message.chat.id, message_id=data.get('message_id'), text=_('Subject teacher:'))
    await AddSubject.teacher.set()


@dp.message_handler(content_types=['text'], state=AddSubject.teacher)
async def add_subject_teacher(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.update_data(teacher=message.text)
    await message.delete()
    await bot.edit_message_text(chat_id=message.chat.id, message_id=data.get('message_id'), text=_('Subject info:'))
    await AddSubject.info.set()


@dp.message_handler(content_types=['text'], state=AddSubject.info)
async def add_subject_teacher(message: Message, state: FSMContext):
    data = await state.get_data()
    add_subject(data.get('name'), data.get('audience'), data.get('teacher'), message.text)
    await message.delete()
    await bot.edit_message_text(chat_id=message.chat.id, message_id=data.get('message_id'), text=_('Subject created'))
    await state.reset_data()
    await state.finish()
