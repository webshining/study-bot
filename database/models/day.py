from pydantic import BaseModel
from .subject import Subject
from loader import database


class Day(BaseModel):
    _id: str
    subjects: list[Subject]


days_collection = database['days']
