from peewee import PrimaryKeyField, CharField
from .base import BaseModel


class User(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    username = CharField()
    status = CharField(default='user')

    class Meta:
        table_name = 'users'
