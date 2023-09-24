from peewee import ForeignKeyField, TimeField, AutoField, IntegerField, CharField, TextField

from .base import BaseModel


class Subject(BaseModel):
    id = AutoField()
    name = CharField()
    audience = CharField()
    teacher = CharField()
    info = TextField(null=True)

    class Meta:
        table_name = 'subjects'


class Day(BaseModel):
    id = AutoField()
    day_id = IntegerField()

    class Meta:
        table_name = 'days'


class DaySubject(BaseModel):
    id = AutoField()
    day = ForeignKeyField(Day, backref='subjects', field='id', on_delete='CASCADE')
    subject = ForeignKeyField(Subject, backref='days', field='id', on_delete='CASCADE')
    subject_order = IntegerField()
    time_start = TimeField()
    time_end = TimeField()

    class Meta:
        table_name = 'days_subjects'
