import calendar
from datetime import datetime, timedelta
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from app.keyboards import get_week_keyboard
from loader import dp
