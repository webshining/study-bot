from pydantic import BaseModel, Field

from loader import db
from .objectid import PydanticObjectId


class Subject(BaseModel):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    name: str
    teacher: str
    audience: str = None
    info: str = None


subjects_collection = db['subjects']
