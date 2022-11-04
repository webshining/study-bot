<<<<<<< HEAD
from aiogram.types import Update
from aiogram.filters import BaseFilter

from data.config import ADMINS


class AdminFilter(BaseFilter):
    def __init__(self):
        self.admins = ADMINS

    def __call__(self, update: Update) -> bool:
        global from_user
        if update.message:
            from_user = update.message.from_user
        if update.callback_query:
            from_user = update.callback_query.from_user
        if update.inline_query:
            from_user = update.inline_query.from_user
        return from_user.id in self.admins
=======
from aiogram.types import Update
from aiogram.filters import BaseFilter

from data.config import ADMINS


class AdminFilter(BaseFilter):
    def __init__(self):
        self.admins = ADMINS

    def __call__(self, update: Update) -> bool:
        global from_user
        if update.message:
            from_user = update.message.from_user
        if update.callback_query:
            from_user = update.callback_query.from_user
        if update.inline_query:
            from_user = update.inline_query.from_user
        return from_user.id in self.admins
>>>>>>> 8ac7a890d7da264576b462a0803f970fa33cd353
