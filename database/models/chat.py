from peewee import AutoField, BigIntegerField, IntegerField

from .base import BaseModel


class Chat(BaseModel):
    id = AutoField()
    chat_id = BigIntegerField(unique=True, )
    group_id = IntegerField(null=True)