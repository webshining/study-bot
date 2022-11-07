from fastapi import APIRouter

from database.models import Day
from database.services import get_day_by_date, get_days

router = APIRouter(prefix='/days')
