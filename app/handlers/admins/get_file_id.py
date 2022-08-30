from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from loader import dp


@dp.message_handler(Command('get_file_id'), status='admin')
async def get_file_id_handler(message: Message):
    if message.reply_to_message.content_type != 'document':
        return await message.reply('Not correct file type!')
    await message.reply(f'<code>{message.reply_to_message.document.file_id}</code>')
