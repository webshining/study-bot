from peewee import CharField, DeferredThroughModel, PrimaryKeyField

from .base import BaseModel

ThroughDeferred = DeferredThroughModel()


class User(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    username = CharField(null=True)
    status = CharField(default='user')
    
    class Meta:
        table_name = 'users'
