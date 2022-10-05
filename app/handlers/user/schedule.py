import calendar
from datetime import datetime, timedelta
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command

from app.keyboards import get_weeks_markup
from database.models import Day
from database.services import get_days
from loader import dp