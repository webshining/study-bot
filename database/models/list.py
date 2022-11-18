from pydantic import BaseModel, Field

from loader import db
from .mongo import PydanticObjectId


class ListElement(BaseModel):
    name: str
    value: str
    user_id: int


class List(BaseModel):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    name: str
    elements: list[ListElement] = []


lists_collection = db["lists"]
