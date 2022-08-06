from peewee import PrimaryKeyField, ManyToManyField
from .base import BaseModel
from .subject import Subject


class Day(BaseModel):
    id = PrimaryKeyField()
    subjects = ManyToManyField(Subject)

    class Meta:
        table_name = 'days'


def init_days():
    if len(list(Day.select())) < 14:
        for i in range(14):
            Day.create()
    return True


DaySubject = Day.subjects.get_through_model()
