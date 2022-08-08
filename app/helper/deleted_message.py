import asyncio

from aiogram.types import Message


async def dmessage(message: Message, text: str, seconds: int):
    message = await message.answer(text)
    for sec in range(seconds - 1, 0, -1):
        await message.edit_text(f'{text} ({sec})')
        await asyncio.sleep(1)
    await message.delete()
