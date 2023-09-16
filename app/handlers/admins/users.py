from aiogram.filters import Command
from aiogram.types import Message

from app.routers import admin_router as router
from database.services import get_users
from loader import _


@router.message(Command('users'))
async def _users(message: Message):
    text, markup = _get_users_data()
    await message.answer(text, reply_markup=markup)


def _get_users_data():
    users = get_users()
    if not users:
        return _('Users is empty🫡'), None
    text = ''
    for user in users:
        text += f'\n{"--" * 15}'
        for key, value in user.dict().items():
            if key == 'username' and value:
                text += f'\n|{key}: <tg-spoiler><b>@{value}</b></tg-spoiler>'
            else:
                text += f'\n|{key}: <b>{value}</b>'
    return text, None
