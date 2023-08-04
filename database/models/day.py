from peewee import IntegerField, PrimaryKeyField

from .base import BaseModel


class Day(BaseModel):
    id = PrimaryKeyField()
    day_id = IntegerField()
    
    class Meta:
        table_name = 'days'
