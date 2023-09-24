from peewee import CharField, DeferredThroughModel, PrimaryKeyField

from .base import BaseModel

ThroughDeferred = DeferredThroughModel()


class User(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    username = CharField(null=True)
    status = CharField(default='user')
    
    @property
    def statuses_to_edit(self):
        statuses = []
        if self.status in ('admin', 'super_admin'):
            statuses.extend(('user', 'banned'))
        if self.status == 'super_admin':
            statuses.extend(('admin', 'banned'))
        return statuses
    
    class Meta:
        table_name = 'users'
