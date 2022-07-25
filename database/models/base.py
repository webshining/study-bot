from peewee import Model
from config.db import database


class BaseModel(Model):
    class Meta:
        database = database
