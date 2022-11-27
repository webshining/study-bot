from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from loader import dp, _
from app.keyboards import lists_markup, list_markup
from database import List, get_lists, get_list


# Get lists
@dp.message(Command('lists'))
async def _lists(message: Message):
    text, markup = _get_lists_data()
    await message.answer(text, reply_markup=markup)


# Get list
@dp.callback_query(lambda call: call.data.startswith('list_get'))
async def _list_get(call: CallbackQuery, is_admin: bool):
    text, markup = _get_list_data(get_list(call.data[9:]), is_admin)
    await call.message.edit_text(text, reply_markup=markup)


# Back list
@dp.callback_query(lambda call: call.data.startswith('list_back'))
async def _list_back(call: CallbackQuery):
    text, markup = _get_lists_data()
    await call.message.edit_text(text, reply_markup=markup)


# Update list
@dp.callback_query(lambda call: call.data.startswith('list_update'))
async def _list_update(call: CallbackQuery, is_admin: bool):
    text, markup = _get_list_data(get_list(call.data[12:]), is_admin)
    try:
        await call.message.edit_text(text, reply_markup=markup)
    except:
        pass


def _get_lists_data():
    lists = get_lists()
    text = _("Select list:") if lists else _("Lists is empty🫡")
    markup = lists_markup('list_get', lists)
    return text, markup.as_markup()


def _get_list_data(list: List, is_admin: bool = False):
    text = _("List not found🫡")
    markup = None
    if list:
        markup = list_markup(list, is_admin).as_markup()
        text = f"<b>{list.name}</b>"
        for element in list.elements:
            text += f'\n{element.key} - {element.value}'
    return text, markup
