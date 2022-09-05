from fastapi import APIRouter

usersRouter = APIRouter(prefix='/users', tags=['Users'])
subjectsRouter = APIRouter(prefix='/subjects', tags=['Subjects'])
daysRouter = APIRouter(prefix='/days', tags=['Days'])

from . import routes
