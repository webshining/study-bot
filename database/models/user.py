from peewee import CharField, IntegerField
from .base import BaseModel


class User(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    username = CharField()
    status = CharField(default='user')
    language = CharField(null=True)

    class Meta:
        table_name = 'users'
