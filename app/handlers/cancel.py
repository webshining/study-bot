from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from loader import _, dp


@dp.message(Command('cancel'))
async def cancel_handler(message: Message, state: FSMContext):
    await message.answer(_("Canceled"))
    await state.set_state(None)
