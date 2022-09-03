from datetime import date
from pydantic import BaseModel, Field
from .pyobjectid import PyObjectId
from .file import File
from loader import database


class Task(BaseModel):
    id: PyObjectId = Field(alias='_id')
    subject: PyObjectId
    text: str
    date: date
    files: list[File] = None


tasks_collection = database['tasks']
