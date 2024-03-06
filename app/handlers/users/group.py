from aiogram import F, html
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from app.keyboards import get_group_markup
from app.routers import user_router as router
from app.states import GroupState
from database.models import User, Group, Timetable, Subject
from loader import _


@router.message(Command("group"))
async def _group(message: Message, user: User, state: FSMContext):
    if not user.group:
        await message.answer(_("You are not a member of the group yet, enter a name to create a new one:"))
        await state.set_state(GroupState.create)
    else:
        text, markup = await _get_group_data(user.group, user.is_admin())
        await message.answer(text, reply_markup=markup)


@router.callback_query(lambda call: call.data.startswith("group"))
async def _group_call(call: CallbackQuery, user: User):
    if call.data[6:] == "subjects":
        text, markup = await _get_subjects_data(user.group, user.is_admin())
    elif call.data[6:] == "delete":
        await User.update(user.id, status="user", group=None)
        await Group.delete({"_id": user.group})
        await Timetable.delete({"group": user.group})
        await Subject.delete({"group": user.group})
        text, markup = _("Success"), None
        return await call.message.edit_text(text, reply_markup=markup)
    await call.message.answer(text, reply_markup=markup)
    await call.answer()


@router.callback_query(lambda call: call.data.startswith("subjects"))
async def _group_subjects(call: CallbackQuery, user: User, state: FSMContext):
    if call.data[9:] == "refresh":
        text, markup = await _get_subjects_data(user.group, user.is_admin())
        try:
            await call.message.edit_text(text, reply_markup=markup)
        except TelegramBadRequest:
            pass
        return await call.answer()
    elif call.data[9:] == "create":
        text, markup = _("Enter subject name:"), None
        await state.set_state(GroupState.subject_name)
    else:
        text, markup = await _get_subject_data(int(call.data[9:]), user.is_admin())
    await call.message.answer(text, reply_markup=markup)
    await call.answer()


@router.callback_query(lambda call: call.data.startswith("subject_"))
async def _group_subject(call: CallbackQuery, user: User, state: FSMContext):
    if call.data[8:].startswith("delete"):
        await Subject.delete({"_id": int(call.data.split("_")[-1])})
        await call.message.delete()
    else:
        pass
    await call.answer()


@router.message(F.text, GroupState.subject_name)
async def _subject_name(message: Message, state: FSMContext):
    await message.answer(_("Enter subject teacher:"))
    await state.update_data(name=message.text)
    await state.set_state(GroupState.subject_teacher)


@router.message(F.text, GroupState.subject_teacher)
async def _subject_teacher(message: Message, state: FSMContext):
    await message.answer(_("Enter subject audience:"))
    await state.update_data(teacher=message.text)
    await state.set_state(GroupState.subject_audience)


@router.message(F.text, GroupState.subject_audience)
async def _subject_name(message: Message, state: FSMContext):
    await message.answer(_("Enter subject info:"))
    await state.update_data(audience=message.text)
    await state.set_state(GroupState.subject_info)


@router.message(F.text, GroupState.subject_info)
async def _subject_name(message: Message, user: User, state: FSMContext):
    data = await state.get_data()
    await Subject.create(name=data.get("name"), teacher=data.get("teacher"), audience=data.get("audience"),
                         info=message.text, group=user.group)
    text, markup = await _get_subjects_data(user.group, user.is_admin())
    await message.answer(text, reply_markup=markup)
    await state.clear()


@router.message(F.text, GroupState.create)
async def _group_create(message: Message, user: User, state: FSMContext):
    await state.clear()
    group = await Group.create(name=message.text)
    await Timetable.init(group.id)
    await User.update(user.id, group=group.id, status="admin")

    text, markup = await _get_group_data(group.id, True)
    await message.answer(text, reply_markup=markup)


async def _get_subjects_data(group: int, is_admin: bool = False):
    subjects = await Subject.get_all(group=group)
    text = _("📚 Subjects") + ":"
    return text, get_group_markup(is_admin, "subjects", subjects)


async def _get_subject_data(id: int, is_admin: bool = False):
    subject = await Subject.get(id)
    if not subject:
        return _('Subject not found🫡'), None
    text = _get_subject_text(subject)
    return text, get_group_markup(is_admin, "subject", id)


def _get_subject_text(subject: Subject):
    text = _('<b>{}:</b>\nTeacher: <b>{}</b>\nAudience: <b>{}</b>').format(subject.name, subject.teacher,
                                                                           subject.audience)
    if subject.info:
        text += f'\n\n{subject.info}'
    return text


async def _get_group_data(group: int, is_admin: bool = False):
    group = await Group.get(group)
    text = f'<b>{html.quote(group.name)}:</b>'
    return text, get_group_markup(is_admin=is_admin)
