from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from loader import dp, _
from app.states import List
from app.filters import AdminFilter
from ..users.lists import _get_list_data
from database import create_list, get_list


# Create new list
@dp.message(AdminFilter(), Command("newlist"))
async def _list_create(message: Message, state: FSMContext):
    await message.answer(_("Enter list name:"))
    await state.set_state(List.create_name)


@dp.message(AdminFilter(), List.create_name)
async def _list_create_name(message: Message, state: FSMContext):
    create_list(message.text)
    await message.answer(_("List created successfully"))
    await state.clear()


# Delete list
@dp.callback_query(AdminFilter(), lambda call: call.data.startswith('list_remove'))
async def _list_remove(call: CallbackQuery):
    _list = get_list((call.data[12:]))
    _list.delete_instance()
    try:
        await call.message.edit_text(_("List deleted successfully"), reply_markup=None)
    except:
        pass


# Edit list
@dp.callback_query(AdminFilter(), lambda call: call.data.startswith('list_edit'))
async def _list_edit(call: CallbackQuery, state: FSMContext):
    await call.message.answer(_("Enter new list name"))
    await state.update_data(id=call.data[10:])
    await state.set_state(List.edit_name)


@dp.message(AdminFilter(), List.edit_name)
async def _list_edit_name(message: Message, state: FSMContext):
    _list = get_list((await state.get_data()).get("id"))
    if _list:
        _list.name = message.text
        _list.save()
        await message.answer(_("List renamed successfully"))
    else:
        await message.answer(_("List not found🫡"))
    await state.clear()


# Edit visible
@dp.callback_query(AdminFilter(), lambda call: call.data.startswith('list_visible'))
async def _list_visible(call: CallbackQuery, is_admin: bool):
    list = get_list(call.data[13:])
    list.visible = not list.visible
    list.save()
    text, markup = _get_list_data(list, is_admin)
    try:
        await call.message.edit_text(text, reply_markup=markup)
    except:
        pass
