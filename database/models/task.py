from pydantic import Field, BaseModel

from .base import Base


class TaskFile(BaseModel):
    file_id: str
    name: str


class Task(Base):
    id: int = Field(alias="_id", default_factory=int)
    text: str
    subject: int
    files: list[TaskFile] = Field([])
