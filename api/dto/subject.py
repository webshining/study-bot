from pydantic import BaseModel

from database.models import File


class SubjectDTO(BaseModel):
    name: str
    audience: str
    teacher: str
    info: str
    files: list[File]
