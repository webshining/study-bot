from pydantic import BaseModel, Field
from loader import database


class User(BaseModel):
    id: int = Field(default_factory=int, alias='_id')
    name: str
    username: str
    status: str


users_collection = database['users']
