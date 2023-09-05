from peewee import BigIntegerField, IntegerField, PrimaryKeyField

from .base import BaseModel


class Chat(BaseModel):
    id = PrimaryKeyField()
    chat_id = BigIntegerField(unique=True, )
    group_id = IntegerField(null=True)