from peewee import CharField, PrimaryKeyField, ForeignKeyField, DateTimeField
from .base import BaseModel
from .subject import Subject


class Task(BaseModel):
    id = PrimaryKeyField()
    text = CharField()
    subject = ForeignKeyField(Subject, null=True)
    date = DateTimeField()

    class Meta:
        table_name = 'tasks'
