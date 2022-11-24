from peewee import PrimaryKeyField, CharField, ForeignKeyField, BooleanField

from .base import BaseModel


class List(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    visible = BooleanField(default=True)
    
    class Meta:
        table_name = 'lists'
    

class ListElement(BaseModel):
    id = PrimaryKeyField()
    list_id = ForeignKeyField(List, backref='elements', on_delete='CASCADE')
    key = CharField()
    value = CharField()
    
    class Meta:
        table_name = 'lists_elements'
