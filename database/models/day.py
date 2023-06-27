from datetime import time

from pydantic import BaseModel, Field, validator

from loader import db
from utils import str_to_time

from .mongo import PydanticObjectId
from .subject import Subject


class DaySubject(BaseModel):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    time_start: time
    time_end: time
    group: str = None
    subject: Subject

    @validator('time_start', 'time_end', pre=True)
    def parse_time(cls, v):
        return str_to_time(v, "%H:%M").time()


class Day(BaseModel):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    subjects: list[DaySubject]
    day_id: int = None


days_collection = db["days"]
