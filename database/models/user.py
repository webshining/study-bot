from peewee import AutoField, BigIntegerField, CharField, DateField

from utils import get_current_time

from .base import BaseModel


class User(BaseModel):
    id = AutoField()
    name = CharField()
    username = CharField(null=True)
    user_id = BigIntegerField(unique=True)
    status = CharField(null=True, default='user')
    updated_at = DateField(default=get_current_time().date())
