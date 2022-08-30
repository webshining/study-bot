from pydantic import BaseModel, Field
from .pyobjectid import PyObjectId
from .subject import Subject
from loader import database


class Day(BaseModel):
    id: PyObjectId = Field(alias='_id')
    subjects: list[Subject] = None


days_collection = database['days']
