from aiogram.filters import Command
from aiogram.types import Message

from app.routers import admin_router as router
from database.services import User, get_users
from loader import _


@router.message(Command('users'))
async def users_handler(message: Message):
    users = get_users()
    text = get_users_text(users)
    await message.answer(text)


def get_users_text(users: list[User]) -> str:
    text = ''
    for user in users:
        text += f'\n{"--" * 20}'
        for key, value in user.__dict__['__data__'].items():
            if key == 'username' and value:
                text += f'\n|{key}: <tg-spoiler><b>@{value}</b></tg-spoiler>'
            else:
                text += f'\n|{key}: <b>{value}</b>'
    return text if text else _('Users is empty🫡')
