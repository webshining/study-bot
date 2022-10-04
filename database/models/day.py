from pydantic import BaseModel, Field

from loader import db
from .subject import Subject
from .objectid import PydanticObjectId


class Day(BaseModel):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    subjects: list[Subject]


days_collection = db['days']
