from peewee import PrimaryKeyField, CharField
from .base import BaseModel


class User(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    username = CharField()
    photo = CharField(null=True)

    class Meta:
        table_name = 'users'
