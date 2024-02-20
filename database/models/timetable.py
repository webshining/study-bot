from datetime import datetime

from pydantic import Field, BaseModel, field_validator

from utils import str_to_time
from .base import Base
from .subject import Subject


class TimetableDaySubject(BaseModel):
    subject: Subject
    time_start: datetime
    time_end: datetime

    @field_validator("time_start", "time_end", mode="before")
    @classmethod
    def parse_time(cls, v: str):
        return str_to_time(v, "%H:%M")


class TimetableDay(BaseModel):
    subjects: list[TimetableDaySubject] = Field([])
    day_id: int


class Timetable(Base):
    id: int = Field(alias="_id", default_factory=int)
    days: list[TimetableDay] = Field([])
    group: int

    @classmethod
    async def get(cls, group: int):
        obj = await cls._collection.aggregate([{"$match": {"group": group}}, *pipeline]).to_list(1)
        obj = next(iter(obj), None)
        return cls(**obj) if obj else obj

    @classmethod
    async def init(cls, group: int):
        await cls.create(group=group, days=[TimetableDay(day_id=i) for i in range(14)])


pipeline = [
    {"$unwind": {"path": "$days", "preserveNullAndEmptyArrays": True}},
    {"$unwind": {"path": "$days.subjects", "preserveNullAndEmptyArrays": True}},
    {"$lookup": {"from": "subjects", "localField": "days.subjects.subject", "foreignField": "_id",
                 "as": "days.subjects.subject"}},
    {"$unwind": {"path": "$days.subjects.subject", "preserveNullAndEmptyArrays": True}},
    {"$group": {"_id": {"_id": "$_id", "day_id": "$days.day_id"}, "group": {"$first": "$group"},
                "subjects": {"$push": "$days.subjects"}}},
    {"$group": {"_id": "$_id._id", "group": {"$first": "$group"},
                "days": {"$push": {"day_id": "$_id.day_id", "subjects": "$subjects"}}}},
    {"$project": {"group": "$group",
                  "days": {"$map": {"input": {"$sortArray": {"input": "$days", "sortBy": {"day_id": 1}}}, "as": "day",
                                    "in": {"$mergeObjects": ["$$day", {"subjects": {
                                        "$sortArray": {"input": {"$cond": {"if": {"$eq": ["$$day.subjects", [{}]]},
                                                                           "then": [],
                                                                           "else": "$$day.subjects"}},
                                                       "sortBy": {"time_start": 1}}}}]}}}}}
]

Timetable.set_collection("timetables")
