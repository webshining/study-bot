from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import dp, _
from app.states import ListStates
from ..users.lists import _get_list_data
from database import create_list, get_list
from data.config import ADMINS


@dp.message(Command('newlist'), F.from_user.id.in_(ADMINS))
async def _list_new(message: Message, state: FSMContext):
    await message.answer(_("Enter list name:"))
    await state.set_state(ListStates.create_name)


@dp.message(ListStates.create_name, F.from_user.id.in_(ADMINS))
async def _list_new_name(message: Message, state: FSMContext):
    create_list(message.text)
    await state.clear()
    await message.answer(_("List <b>{}</b> created").format(message.text))


@dp.callback_query(lambda call: call.data.startswith(('list_turn', 'list_rename', 'list_delete')), F.from_user.id.in_(ADMINS))
async def _list_admin(call: CallbackQuery, state: FSMContext, is_admin: bool):
    if call.data.startswith('list_turn'):
        id = call.data[10:]
        lst = get_list(id)
        lst.visible = not lst.visible
        lst.save()
        text, markup = _get_list_data(lst, is_admin)
        try:
            await call.message.edit_text(text, reply_markup=markup)
        except:
            pass
    elif call.data.startswith('list_rename'):
        id = call.data[12:]
        lst = get_list(id)
        if not lst:
            text, markup = _get_list_data(lst, is_admin)
            await call.message.edit_text(text, reply_markup=markup)
        else:
            await state.update_data(id=lst.id)
            await state.set_state(ListStates.edit_name)
            await call.message.answer("Enter new name:")
    elif call.data.startswith('list_delete'):
        id = call.data[12:]
        lst = get_list(id)
        lst.delete_instance()
        await call.message.edit_text(_("List deleted🫡"), reply_markup=None)


@dp.message(ListStates.edit_name, F.from_user.id.in_(ADMINS))
async def _list_rename(message: Message, state: FSMContext, is_admin: bool):
    lst = get_list((await state.get_data()).get("id"))
    if lst:
        lst.name = message.text
        lst.save()
        await message.answer(_("List renamed🫡"))
    else:
        text, markup = _get_list_data(lst)
        await message.answer(text, reply_markup=markup)
    await state.clear()
