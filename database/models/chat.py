from peewee import PrimaryKeyField, DecimalField, IntegerField

from .base import BaseModel


class Chat(BaseModel):
    id = PrimaryKeyField()
    chatId = DecimalField(max_digits=20)
    facultyId = IntegerField()
    courseId = IntegerField()
    groupId = IntegerField()