from pydantic import BaseModel, Field
from loader import db


class User(BaseModel):
    id: int = Field(default_factory=int, alias="_id")
    name: str
    username: str
    status: str = None


users_collection = db['users']
