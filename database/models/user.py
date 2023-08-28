from peewee import (BigIntegerField, CharField, DeferredThroughModel,
                    IntegerField, PrimaryKeyField)

from .base import BaseModel

ThroughDeferred = DeferredThroughModel()


class User(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    user_id = IntegerField(unique=False)
    chat_id = BigIntegerField()
    status = CharField(null=True, default='user')
