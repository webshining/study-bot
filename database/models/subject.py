from pydantic import BaseModel, Field
from .file import File
from .objectid import PyObjectId
from loader import db


class Subject(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    audience: str
    teacher: str
    info: str
    files: list[File]
    time_start: str = None
    time_end: str = None


subjects_collection = db['subjects']
