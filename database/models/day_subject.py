from peewee import CharField, ForeignKeyField, TimeField

from .base import BaseModel
from .day import Day
from .subject import Subject


class DaySubject(BaseModel):
    day = ForeignKeyField(Day, backref='subjects', field='id', on_delete='CASCADE')
    subject = ForeignKeyField(Subject, backref='days', field='id', on_delete='CASCADE')
    time_start = TimeField()
    time_end = TimeField()
    group = CharField(null=True)
    
    class Meta:
        table_name = 'days_subjects'
