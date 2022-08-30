from pydantic import BaseModel
from database import File


class Subject(BaseModel):
    name: str
    audience: str
    teacher: str
    info: str = None
    files: list[File] = None
