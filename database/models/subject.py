from pydantic import Field, BaseModel

from .base import Base


class SubjectFile(BaseModel):
    file_id: str
    name: str


class Subject(Base):
    id: int = Field(alias="_id", default_factory=int)
    name: str
    audience: str
    teacher: str
    info: str | None = Field(None)
    group: int
    files: list[SubjectFile] = Field([])


Subject.set_collection("subjects")
