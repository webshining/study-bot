from pydantic import BaseModel


class SubjectPatch(BaseModel):
    name: str
    audience: str
    teacher: str
    info: str = None


class SubjectCreate(BaseModel):
    name: str
    audience: str
    teacher: str
    info: str = None
