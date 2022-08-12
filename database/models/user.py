from peewee import CharField, PrimaryKeyField
from .base import BaseModel


class User(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    username = CharField()
    language = CharField(default='en')
    status = CharField(default='user')

    class Meta:
        table_name = 'users'
