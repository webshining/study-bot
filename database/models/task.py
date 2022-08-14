from peewee import PrimaryKeyField, ForeignKeyField, TextField, DateTimeField
from .base import BaseModel
from .subject import Subject


class Task(BaseModel):
    id = PrimaryKeyField()
    text = TextField()
    subject = ForeignKeyField(Subject, backref='tasks')
    date = DateTimeField()

    class Meta:
        table_name = 'tasks'
