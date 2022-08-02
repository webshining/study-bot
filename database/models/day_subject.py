from peewee import PrimaryKeyField, ForeignKeyField
from .base import BaseModel
from .subject import Subject
from .day import Day


class DaySubject(BaseModel):
    day = ForeignKeyField(Day)
    subject = ForeignKeyField(Subject)

    class Meta:
        table_name = 'day_subject'
