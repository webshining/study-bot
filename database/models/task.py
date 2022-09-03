from datetime import date
from pydantic import BaseModel, Field
from .pyobjectid import PyObjectId
from .file import File
from .subject import Subject
from loader import database


class Task(BaseModel):
    id: PyObjectId = Field(alias='_id')
    subject: Subject
    text: str
    date: date
    files: list[File] = None


tasks_collection = database['tasks']
