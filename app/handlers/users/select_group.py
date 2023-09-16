from aiogram.filters import Command
import pickle
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.keyboards import get_select_markup
from app.routers import user_router as router
from database.services import update_chat
from loader import _
from utils import get_courses, get_faculties, get_groups


@router.message(Command('select_group'))
@router.message(lambda message: message.text == _('Select Group 👥'))
async def group_handler(message: Message, state: FSMContext, redirect: any = None):
    text = _('Select faculty:')
    faculties = get_faculties()
    if not faculties:
        return await message.answer(_("It seems the servers are not responding, and there is no saved data for you🫡"))
    await message.answer(text, reply_markup=get_select_markup('faculty', faculties, key_text='name'))
    await state.clear()
    if redirect:
        await state.update_data(redirect=pickle.dumps(redirect).hex())


@router.callback_query(lambda call: call.data.startswith('faculty'))
async def faculty_callback(call: CallbackQuery, state: FSMContext):
    courses = get_courses(call.data[8:])
    if not courses:
        return await call.message.edit_text(
            _("It seems the servers are not responding, and there is no saved data for you🫡"))
    await call.message.edit_text(_('Select course:'),
                                 reply_markup=get_select_markup('course', courses, key_text='name'))
    await state.update_data(faculty=call.data[8:])


@router.callback_query(lambda call: call.data.startswith('course'))
async def course_callback(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    faculty = data.get('faculty')
    groups = get_groups(faculty, call.data[7:])
    if not groups:
        return await call.message.edit_text(
            _("It seems the servers are not responding, and there is no saved data for you🫡"))
    await call.message.edit_text(_('Select group:'), reply_markup=get_select_markup('group', groups, key_text='name'))


@router.callback_query(lambda call: call.data.startswith('group'))
async def group_callback(call: CallbackQuery, state: FSMContext, group_id, user):
    if group_id != int(call.data[6:]):
        user.status = 'user'
        user.save()
        if 'group' in call.message.chat.type:
            if call.from_user.id in [i.user.id for i in await call.message.chat.get_administrators()]:
                update_chat(call.message.chat.id, call.data[6:])
            else:
                update_chat(call.from_user.id, call.data[6:])
        else:
            update_chat(call.from_user.id, call.data[6:])
    text, markup = (_("Success"), None)
    redirect = (await state.get_data()).get('redirect')
    if redirect:
        text, markup = await pickle.loads(bytes.fromhex(redirect))(call.data[6:], state=state)
    await call.message.edit_text(text, reply_markup=markup)
