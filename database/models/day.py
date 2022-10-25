from pydantic import BaseModel, Field

from loader import db
from .subject import Subject
from .objectid import PydanticObjectId

class DaySubject(BaseModel):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    time_start: str
    time_end: str
    subject: Subject
    
class Day(BaseModel):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    subjects: list[DaySubject]
    day_id: int = None


days_collection = db["days"]
