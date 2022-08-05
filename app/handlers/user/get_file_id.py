import asyncio
from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from loader import dp, _, bot
from utils import dmessage


@dp.message_handler(Command('get_file_id'))
async def get_file_id_handler(message: Message):
    await message.delete()
    if not message.reply_to_message:
        await dmessage(message, _('Message should be a reply'), 5)
    elif message.reply_to_message.content_type == 'document':
        await message.answer(f'<pre>{message.reply_to_message.document.file_id}</pre>')
    else:
        await message.answer(f'Мне нужен документ, а вы отправили {message.reply_to_message.content_type}')
