from peewee import Model
from playhouse.shortcuts import model_to_dict

from loader import database


class BaseModel(Model):

    def to_dict(self):
        return model_to_dict(self)

    class Meta:
        database = database
