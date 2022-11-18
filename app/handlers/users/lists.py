import re
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from loader import dp, bot
from app.keyboards import get_lists_makrup, get_update_makrup, get_to_private_makrup
from app.states import AddToList
from database import get_lists, get_list, push_list_element, List as ListModel

# Get lists
@dp.message(Command('lists'))
async def _lists(message: Message):
    text, markup = _get_lists_data()
    await message.answer(text, reply_markup=markup)
    
    
@dp.callback_query(lambda call: call.data.startswith('lists_get') or call.data.startswith('lists_upd'))
async def _list(call: CallbackQuery):
    await call.answer()
    _list = get_list(call.data[10:])
    text = _get_list_text(_list) if _list else "List not found"
    try:
        markup = get_update_makrup('lists_upd', call.data[10:])
        if call.data[6:].startswith('upd'):
            if call.inline_message_id:
                return await bot.edit_message_text(text=text, inline_message_id=call.inline_message_id, reply_markup=markup)
            await call.message.edit_text(text=text, reply_markup=markup)
        else:
            if call.inline_message_id:
                return await bot.edit_message_text(text=text, inline_message_id=call.inline_message_id, reply_markup=markup)
            await call.message.edit_text(text=text, reply_markup=markup)
    except:
        pass

# Add element to list
@dp.message(Command("lists_set"))
async def _lists_set(message: Message):
    if message.chat.type != 'private':
        return message.answer("In order to avoid all the bad, please go to private chat", reply_markup=get_to_private_makrup())
    lists = get_lists()
    await message.answer("Select list:" if lists else "Lists is emty", reply_markup=get_lists_makrup('lists_set', lists) if lists else None)


@dp.callback_query(lambda call: call.data.startswith('lists_set'))
async def _list_set(call: CallbackQuery, state: FSMContext):
    _list = get_list(call.data[10:])
    await state.update_data(id=_list.id)
    await call.message.edit_text("Enter your name and value <b>[Kashey Immortal - world literature]</b>:" if _list else "List not found", reply_markup=None)
    if _list:
        await state.set_state(AddToList.text)


@dp.message(AddToList.text)
async def _list_set_value(message: Message, state: FSMContext):
    id = (await state.get_data()).get('id')
    match = re.match("(.*) - (.*)", message.text)
    if match:
        push_list_element(id, match[1], match[2], message.from_user.id)
        await message.answer("Lists updated")
        await state.clear()
    else:
        await message.answer("Incorrect input data format, please enter correctly")


def _get_list_text(list: ListModel):
    text = f"<b>{list.name}</b>"
    for element in list.elements:
        text += f'\n{element.name} - {element.value}'
    if not list.elements:
        text += f'\nList is empty🫡'
    
    return text
        
    

def _get_lists_data():
    lists = get_lists()
    markup = get_lists_makrup('lists_get', lists) if lists else None
    
    return "Select list:" if lists else "Lists is empty🫡", markup
