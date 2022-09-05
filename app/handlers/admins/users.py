from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from loader import dp, _
from database import get_users


@dp.message_handler(Command('users'), status='admin')
async def get_all_users_handler(message: Message):
    users = await get_users()
    await message.answer(_get_users_text(users))


def _get_users_text(users: list):
    text = ''
    for user in users:
        text += f'\n\n<b>{user.name}:</b>\nid: <code>{user.id}</code>'
        if user.username:
            text += f'\nusername: <b>@{user.username}</b>'
        text += f'\nstatus: <b>{user.status}</b>'

    return text if text != '' else "Users list is empty!"
