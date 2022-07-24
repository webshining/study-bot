from aiogram import Bot, Dispatcher, types
from config import TELEGRAM_BOT_TOKEN, ADMINS
from app.middlewares.i18n import i18n

bot = Bot(TELEGRAM_BOT_TOKEN, disable_web_page_preview=True, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

_ = i18n.gettext
