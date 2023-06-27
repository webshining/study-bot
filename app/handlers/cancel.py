from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.routers import user_router as router
from loader import _


@router.message(Command('cancel'))
async def _cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(_("State reset"))
