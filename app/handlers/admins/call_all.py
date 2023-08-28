from aiogram.filters import Command
from aiogram.types import Message

from app.routers import admin_router as router
from database.services import get_users
from loader import _


@router.message(Command('call_all'))
async def start_handler(message: Message, user):
    members = get_users(message.chat.id)
    text = _("Listen to everyone!")+"\n"
    for member in members:
        text += f'<a href="tg://user?id={member.user_id}">ㅤ</a>'
    await message.answer(text)
