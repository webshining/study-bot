from peewee import PrimaryKeyField, ManyToManyField, ForeignKeyField
from .base import BaseModel
from .subject import Subject


class Day(BaseModel):
    id = PrimaryKeyField()
    subjects = ManyToManyField(Subject)

    class Meta:
        table_name = 'days'


class DaySubjectThrough(BaseModel):
    day = ForeignKeyField(Day, unique=False)
    subject = ForeignKeyField(Subject, unique=False)

    class Meta:
        table_name = 'days_subjects_through'


def init_days():
    if len(list(Day.select())) < 14:
        for i in range(14):
            Day.create()
    return True


Day.subjects.through_model = DaySubjectThrough
