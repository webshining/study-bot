from fastapi import APIRouter

subjectsRouter = APIRouter(prefix='/api', tags=['Subjects'])

from .routes import *
