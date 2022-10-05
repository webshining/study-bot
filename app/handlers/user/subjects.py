from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from app.keyboards import get_subjects_markup
from database.models import Subject
from database.services import get_subjects, get_subject
from loader import dp