from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from loader import _, dp


@dp.message(Command('cancel'))
async def cancel_handler(message: Message, state: FSMContext):
    await state.set_state(None)
    await message.answer(_("State reset"))
