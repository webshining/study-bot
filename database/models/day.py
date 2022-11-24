from peewee import PrimaryKeyField, IntegerField, DeferredThroughModel, ManyToManyField

from .subject import Subject
from .base import BaseModel

ThroughDeferred = DeferredThroughModel()


class Day(BaseModel):
    id = PrimaryKeyField()
    day_id = IntegerField()
    
    class Meta:
        table_name = 'days'
