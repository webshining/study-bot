from peewee import IntegerField, CharField
from .base import BaseModel


class Day(BaseModel):
    id = IntegerField(primary_key=True)
    subjects = CharField(default='')

    class Meta:
        table_name = 'days'


def init_days():
    if len(list(Day.select())) != 14:
        for i in range(14):
            Day.create()
