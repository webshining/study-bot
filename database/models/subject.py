from peewee import CharField, PrimaryKeyField, TextField

from .base import BaseModel


class Subject(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    audience = CharField()
    teacher = CharField()
    info = TextField(null=True)
    
    class Meta:
        table_name = 'subjects'
