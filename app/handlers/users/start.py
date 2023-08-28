from aiogram.filters import Command
from aiogram.types import Message

from app.routers import user_router as router
from loader import _


@router.message(Command('start'))
async def start_handler(message: Message):
    text = _('Hello <b>{}</b>👋\nWrite /help to see more information').format(message.from_user.full_name)
    await message.answer(text)
