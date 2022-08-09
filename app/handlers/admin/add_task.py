from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup

from loader import dp, _
from database import get_subjects
from app.keyboards import get_subjects_markup
