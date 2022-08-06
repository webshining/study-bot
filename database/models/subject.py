from peewee import PrimaryKeyField, CharField
from .base import BaseModel


class Subject(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    audience = CharField()
    teacher = CharField()
    info = CharField(null=True)

    class Meta:
        table_name = 'subjects'
