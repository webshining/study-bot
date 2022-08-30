from pydantic import BaseModel, Field
from .pyobjectid import PyObjectId
from .file import File
from loader import database


class Task(BaseModel):
    id: PyObjectId = Field(alias='_id')
    subject: PyObjectId
    text: str
    files: list[File] = None


tasks_collection = database['tasks']
