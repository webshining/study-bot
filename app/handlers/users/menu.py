from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from loader import _
from app.routers import user_router as router
from app.keyboards import get_menu_markup


@router.message(Command('menu_on'))
async def menu_on_handler(message: Message):
    await message.answer(_("Success"), reply_markup=get_menu_markup())


@router.message(Command('menu_off'))
async def menu_on_handler(message: Message):
    await message.answer(_("Success"), reply_markup=ReplyKeyboardRemove())
