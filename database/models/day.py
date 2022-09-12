from pydantic import BaseModel, Field
from . import Subject
from .objectid import PyObjectId
from loader import db


class Day(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    subjects: list[Subject]


days_collection = db['days']
