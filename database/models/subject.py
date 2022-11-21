from peewee import PrimaryKeyField, CharField, TextField

from .base import BaseModel


class Subject(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    audience = CharField()
    teacher = CharField()
    info = TextField(null=True)
