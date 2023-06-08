from peewee import BigIntegerField, CharField, IntegerField, PrimaryKeyField

from .base import BaseModel


class User(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    user_id = IntegerField(unique=False)
    chat_id = BigIntegerField()
    status = CharField(null=True, default='user')
