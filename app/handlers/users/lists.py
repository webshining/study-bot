from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.filters import Command

from loader import dp, _
from database import List, get_lists, get_list
from app.keyboards import get_lists_markup, get_update_markup


@dp.message(Command("lists"))
async def _lists(message: Message):
    text, markup = _get_lists_data()
    await message.answer(text, reply_markup=markup)
    
    
@dp.callback_query(lambda call: call.data.startswith('list') and not call.data.startswith('list_settings'))
async def _lists_callback(call: CallbackQuery, is_admin: bool):
    await call.answer()
    if call.data.startswith('list_update'):
        id = call.data[12:]
    else:
        id = call.data[5:]
    text, markup = _get_list_data(get_list(id), is_admin)
    try:
        await call.message.edit_text(text, reply_markup=markup)
    except:
        pass


def _get_list_data(list: List, is_admin: bool = False):
    text = _('List not found🫡')
    markup = None
    if list:
        text = f'<b>{list.name}</b>'
        for element in list.elements:
            text += f'\n{element.key} - {element.value}'
            
        markup = get_update_markup(f'list_update_{list.id}')
        if is_admin:
            markup.add(InlineKeyboardButton(text=_('⚙️Settings'), callback_data=f'list_settings_{list.id}'))
        markup = markup.as_markup()
    return text, markup
    

def _get_lists_data():
    lists = get_lists()
    markup = get_lists_markup('list', lists)
    return _('Select list:') if lists else _("Lists is empty🫡"), markup