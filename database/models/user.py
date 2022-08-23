from pydantic import BaseModel
from loader import database


class User(BaseModel):
    _id: str
    user_id: int
    name: str
    username: str
    status: str
    

users = database['users']
