from pydantic import BaseModel, Field
from .objectid import PyObjectId
from .user import User
from loader import db


class Group(BaseModel):
    id: str = Field(default_factory=PyObjectId, alias='_id')
    name: str
    users: list[User]


groups_collection = db['groups']