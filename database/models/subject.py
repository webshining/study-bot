from pydantic import BaseModel, Field
from .pyobjectid import PyObjectId
from .file import File
from loader import database


class Subject(BaseModel):
    id: PyObjectId = Field(alias='_id')
    name: str
    audience: str
    teacher: str
    info: str = None
    files: list[File] = None


subjects_collection = database['subjects']
