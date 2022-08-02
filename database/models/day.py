from peewee import PrimaryKeyField
from .base import BaseModel


class Day(BaseModel):
    id = PrimaryKeyField()

    class Meta:
        table_name = 'days'
