from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from loader import dp


@dp.message(Command('cancel'))
async def _cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("State reset")
