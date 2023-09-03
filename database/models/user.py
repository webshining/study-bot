from peewee import (CharField, DeferredThroughModel, IntegerField,
                    PrimaryKeyField)

from .base import BaseModel

ThroughDeferred = DeferredThroughModel()


class User(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    username = CharField(null=True)
    user_id = IntegerField(unique=True)
    status = CharField(null=True, default='user')
