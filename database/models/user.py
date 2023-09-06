from peewee import (AutoField, BigIntegerField, CharField,
                    DeferredThroughModel, IntegerField)

from .base import BaseModel

ThroughDeferred = DeferredThroughModel()


class User(BaseModel):
    id = AutoField()
    name = CharField()
    username = CharField(null=True)
    user_id = BigIntegerField(unique=True)
    status = CharField(null=True, default='user')
