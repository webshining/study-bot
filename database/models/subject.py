from pydantic import BaseModel, Field

from loader import db
from .mongo import PydanticObjectId


class Subject(BaseModel):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id") or None
    name: str
    audience: str
    teacher: str
    info: str


subjects_collection = db['subjects']
