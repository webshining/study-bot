from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from loader import dp
from app.keyboards import get_lists_makrup
from database import get_lists, get_list, List as ListModel


@dp.message(Command('lists'))
async def _lists(message: Message):
    text, markup = _get_lists_data()
    await message.answer(text, reply_markup=markup)
    
    
@dp.callback_query(lambda call: call.data.startswith('lists_get'))
async def _list(call: CallbackQuery):
    await call.answer()
    _list = get_list(call.data[10:])
    text = _get_list_text(_list) if _list else "List not found"
    await call.message.edit_text(text=text, reply_markup=None)
    
    
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
