from peewee import AutoField, CharField, ForeignKeyField

from .base import BaseModel
from .task import Task


class File(BaseModel):
    id = AutoField()
    file_id = CharField(null=False)
    file_type = CharField(null=False)
    task = ForeignKeyField(Task, backref='files', null=False, field="id", on_delete='CASCADE')
