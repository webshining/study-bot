from peewee import ManyToManyField, ForeignKeyField, IntegerField
from .base import BaseModel
from .subject import Subject


class Day(BaseModel):
    id = IntegerField(primary_key=True)
    subjects = ManyToManyField(Subject, backref='days')

    class Meta:
        table_name = 'week'


class DaySubjectThrough(BaseModel):
    day = ForeignKeyField(Day, unique=False)
    subject = ForeignKeyField(Subject, unique=False)
    subject_number = IntegerField(unique=False)

    class Meta:
        table_name = 'week_subjects_through'


Day.subjects.through_model = DaySubjectThrough


def init_week():
    if len(list(Day.select())) != 14:
        for i in range(14):
            Day.create()

    return
