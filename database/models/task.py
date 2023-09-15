from peewee import AutoField, CharField, BooleanField, DateField, TextField, ForeignKeyField

from .base import BaseModel
from .user import User


class Task(BaseModel):
    id = AutoField()
    name = CharField(null=False, default="")
    text = TextField(null=False)
    date = DateField(null=False)
    group_id = CharField(null=False)
    confirmed = BooleanField(default=False)
    creator = ForeignKeyField(User, backref='tasks', on_delete='CASCADE', default=None, null=True)
