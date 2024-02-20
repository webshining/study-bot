from aiogram.filters import Filter
from aiogram.types import Update


class AdminFilter(Filter):
    async def __call__(self, update: Update, **data) -> bool:
        user = data['user']
        _is = user.is_admin()
        return _is
