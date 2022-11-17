from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from loader import dp
from app.states import CreateList, EditList
from app.filters import AdminFilter
from app.keyboards import get_lists_makrup
from database import get_lists, get_list, create_list, edit_list, delete_list

# Create list
@dp.message(AdminFilter(), Command('create_list'))
async def _list_create(message: Message, state: FSMContext):
    await message.answer("Enter list name:")
    await state.set_state(CreateList.name)
    

@dp.message(CreateList.name)
async def _list_create_name(message: Message, state: FSMContext):
    create_list(message.text)
    await message.answer(f'List <b>{message.text}</b> created')
    await state.clear()
    
# Edit list
@dp.message(AdminFilter(), Command('edit_list'))
async def _lists_edit(message: Message):
    lists = get_lists()
    await message.answer("Select the list you want to change:" if lists else "Lists is empty", reply_markup=get_lists_makrup('lists_ed', lists) if lists else None)
    
    
@dp.callback_query(lambda call: call.data.startswith('lists_ed'))
async def _list_edit(call: CallbackQuery, state: FSMContext):
    await call.answer()
    _list = get_list(call.data[9:])
    if _list:
        await call.message.edit_text("Enter new name:", reply_markup=None)
        await state.update_data(id=call.data[9:], old_name=_list.name)
        await state.set_state(EditList.name)
    else:
        await call.message.edit_text("List not found")
        await state.clear()
    

@dp.message(EditList.name)
async def _list_edit_name(message: Message, state: FSMContext):
    data = await state.get_data()
    edit_list(data.get("id"), message.text)
    await message.answer(f'List <b>{data.get("old_name")}</b> renamed to <b>{message.text}</b>')
    await state.clear()
    
# Delete list
@dp.message(AdminFilter(), Command('delete_list'))
async def _lists_delete(message: Message):
    lists = get_lists()
    await message.answer("Select list to delete:" if lists else "Lists is empty", reply_markup=get_lists_makrup("lists_del", lists) if lists else None)


@dp.callback_query(lambda call: call.data.startswith("lists_del"))
async def _list_delete(call: CallbackQuery):
    await call.answer()
    name = get_list(call.data[10:]).name
    await call.message.edit_text(f"List <b>{name}</b> deleted", reply_markup=None)
    delete_list(call.data[10:])
    