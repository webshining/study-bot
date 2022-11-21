from peewee import ForeignKeyField, TimeField

from .day import Day
from .subject import Subject

from .base import BaseModel


class DaySubject(BaseModel):
    day = ForeignKeyField(Day, backref='subjects', field='id', on_delete='CASCADE')
    subject = ForeignKeyField(Subject, backref='days', field='id', on_delete='CASCADE')
    time_start = TimeField()
    time_end = TimeField()
