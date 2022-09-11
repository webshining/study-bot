from pydantic import BaseModel, Field
from loader import database


class User(BaseModel):
    id: int = Field(alias='_id')
    name: str
    username: str = None
    status: str


users_collection = database['users']