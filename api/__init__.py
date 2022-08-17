from fastapi import APIRouter

router = APIRouter(prefix='/api', tags=["api"])

from . import subjects
from . import users
