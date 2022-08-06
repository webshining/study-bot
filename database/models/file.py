from peewee import ForeignKeyField, PrimaryKeyField, CharField
from .base import BaseModel
from .subject import Subject


class File(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    file_id = CharField()
    subject = ForeignKeyField(Subject, backref='files', null=True)

    class Meta:
        table_name = 'files'
