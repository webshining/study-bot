from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from loader import dp, _
from app.states import ListCreate
from database import create_list


@dp.message(Command("list_create"))
async def _list_create(message: Message, state: FSMContext):
    await message.answer(_("Enter list name:"))
    await state.set_state(ListCreate.name)


@dp.message(ListCreate.name)
async def _list_create_name(message: Message, state: FSMContext):
    create_list(message.text)
    await message.answer(_("List created successfully"))
    await state.clear()