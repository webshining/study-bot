from aiogram.types import CallbackQuery

from loader import dp, _
from app.filters import AdminFilter


@dp.callback_query(AdminFilter(), lambda call: call.data.startswith('list_settings'))
async def _list_settings(call: CallbackQuery):
    await call.answer("ok")