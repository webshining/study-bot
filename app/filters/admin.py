from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter

from data.config import ADMINS


class AdminFilter(BoundFilter):
    key = 'is_admin'
    
    def __init__(self):
        self.admins = ADMINS
    
    def check(self, message: Message) -> bool:
        return message.from_user.id in self.admins