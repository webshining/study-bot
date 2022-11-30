import re
import asyncio
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from loader import dp, _
from app.states import ListStates
from app.keyboards import lists_markup, list_markup
from database import List, get_lists, get_list, add_entry


# Get list
@dp.message(Command('lists'))
async def _lists(message: Message, is_admin: bool):
    text, markup = _get_lists_data(is_admin)
    await message.answer(text, reply_markup=markup)


@dp.callback_query(lambda call: call.data.startswith(('list_get', 'list_update', 'list_back', 'list_write')))
async def _list(call: CallbackQuery, state: FSMContext, is_admin: bool):
    await call.answer(call.data)
    if call.data.startswith('list_get'):
        text, markup = _get_list_data(get_list(call.data[9:]), is_admin)
    elif call.data.startswith('list_update'):
        text, markup = _get_list_data(get_list(call.data[12:]), is_admin)
    elif call.data.startswith('list_back'):
        text, markup = _get_lists_data(is_admin)
    elif call.data.startswith('list_write'):
        lst = get_list(call.data[11:])
        if lst:
            message = await call.message.answer(_("Send a Key - Value format message:"))
            await state.update_data(id=call.data[11:])
            await state.set_state(ListStates.write)
            await asyncio.sleep(60)
            await message.delete()
        else:
            text, markup = _get_list_data(lst)
            await call.message.edit_text(text, reply_markup=markup)
        return
    try:
        await call.message.edit_text(text, reply_markup=markup)
    except:
        pass


@dp.message(ListStates.write)
async def _list_write_text(message: Message, state: FSMContext):
    match = re.match("(.+) - (.+)", message.text)
    if match:
        add_entry(match[1], match[2], (await state.get_data()).get("id"), message.from_user.id)
        message = await message.answer(_("Entry added to the list"))
        await state.clear()
        await asyncio.sleep(60)
        await message.delete()
    else:
        await message.answer(_("You entered an invalid string, please try again"))


def _get_list_data(lst: List, is_admin: bool = False):
    text = _("List not found🫡")
    markup = None
    if lst:
        markup = list_markup(lst, is_admin).as_markup()
        text = f'<b>{lst.name}</b>'
        for element in lst.elements:
            text += f'\n{element.key} - {element.value}'
    return text, markup


def _get_lists_data(is_admin: bool = False):
    lists = get_lists(is_admin)
    text = _("Select list:") if lists else _("Lists is empty🫡")
    markup = lists_markup("list_get", lists)
    return text, markup.as_markup()
