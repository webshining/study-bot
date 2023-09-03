from peewee import (CharField, DeferredThroughModel, IntegerField,
                    PrimaryKeyField)

from .base import BaseModel

ThroughDeferred = DeferredThroughModel()


class Chat(BaseModel):
    id = PrimaryKeyField()
    chat_id = IntegerField(unique=True)
    group_id = CharField(null=True)
