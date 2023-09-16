from peewee import AutoField, CharField, DateField, TextField, ForeignKeyField

from .base import BaseModel
from .user import User


class Task(BaseModel):
    id = AutoField()
    name = CharField(null=False, default="")
    text = TextField(null=False)
    date = DateField(null=False)
    group_id = CharField(null=False)
    status = CharField(default='confirm')
    creator = ForeignKeyField(User, backref='tasks', on_delete='CASCADE', default=None, null=True)
