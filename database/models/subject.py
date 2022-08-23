from pydantic import BaseModel
from loader import database


class Subject(BaseModel):
    _id: str
    codename: str
    name: str
    audience: str
    teacher: str
    info: str
    

subjects = database['subjects']
    