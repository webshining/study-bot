from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.models import File


def get_files_makrup(data: str, files: list[File]):
    builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text=file.name, callback_data=f'{data}_{file.file_id}') for file in files
    ]
    builder.add(*buttons)
    builder.adjust(3)
    return builder.as_markup()
