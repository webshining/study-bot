from pydantic import BaseModel, Field

from loader import db

from .mongo import PydanticObjectId


class User(BaseModel):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id") or None
    user_id: int
    name: str
    username: str = None
    status: str


users_collection = db['users']
