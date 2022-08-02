from peewee import PrimaryKeyField, CharField
from .base import BaseModel


class Subject(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    audience = CharField(null=True)
    teacher = CharField(null=True)
    info = CharField(null=True)

    class Meta:
        table_name = 'subjects'
