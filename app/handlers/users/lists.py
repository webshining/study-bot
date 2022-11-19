import re
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from loader import dp, bot
from app.keyboards import get_lists_makrup, get_update_markup
from app.states import AddToList
from database import get_lists, get_list, push_list_element, List as ListModel


# Get lists
@dp.message(Command('lists'))
async def _lists(message: Message):
    text, markup = _get_lists_data("Select a list to view:", 'lists_get')
    await message.answer(text, reply_markup=markup)


@dp.callback_query(lambda call: call.data.startswith('lists_get'))
async def _lists_list(call: CallbackQuery):
    await call.answer()
    _list = get_list(call.data[10:])
    text, markup = _get_list_data(_list)
    try:
        if call.inline_message_id:
            return await bot.edit_message_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
        await call.message.edit_text(text, reply_markup=markup)
    except:
        pass


# Add element to list
@dp.message(Command("lists_set"))
async def _lists_set(message: Message):
    text, markup = _get_lists_data("Select a list to set:", 'lists_set')
    await message.answer(text, reply_markup=markup)


@dp.callback_query(lambda call: call.data.startswith('lists_set'))
async def _lists_set_callback(call: CallbackQuery, state: FSMContext):
    await call.answer()
    _list = get_list(call.data[10:])
    if _list:
        await state.clear()
        await call.message.answer(f"<b>{call.from_user.full_name}</b> enter the format string <b>Name - Value</b>:")
        await state.update_data(id=_list.id)
        await state.set_state(AddToList.text)
    else:
        await call.message.edit_text("List not found or deleted", reply_markup=None)


@dp.message(AddToList.text)
async def _list_set_text(message: Message, state: FSMContext):
    match = re.match("(.*) - (.*)", message.text)
    if match:
        id = (await state.get_data()).get('id')
        list = get_list(id)
        if list:
            push_list_element(id, match[1], match[2], message.from_user.id)
            await message.answer("Lists updated")
        else:
            await message.answer("List not found or deleted")
        await state.clear()
    else:
        await message.answer("Incorrect input data format, please enter correctly")


def _get_list_data(list: ListModel | None):
    text = "List not found"
    markup = None
    if list:
        text = f"List <b>{list.name}</b> is empty"
        markup = get_update_markup('lists_get', list.id)
        if list.elements:
            text = f'<b>{list.name}</b>'
            for element in list.elements:
                text += f'\n{element.name} - {element.value}'
    return text, markup


def _get_lists_data(text: str, data: str):
    lists = get_lists()
    markup = get_lists_makrup(data, lists) if lists else None

    return text if lists else "Lists is empty🫡", markup
