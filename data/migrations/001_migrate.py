"""Peewee migrations -- 001_migrate.py.

Some examples (model - class or model name)::

    > Model = migrator.orm['model_name']            # Return model in current state by name

    > migrator.sql(sql)                             # Run custom SQL
    > migrator.python(func, *args, **kwargs)        # Run python code
    > migrator.create_model(Model)                  # Create a model (could be used as decorator)
    > migrator.remove_model(model, cascade=True)    # Remove a model
    > migrator.add_fields(model, **fields)          # Add fields to a model
    > migrator.change_fields(model, **fields)       # Change fields
    > migrator.remove_fields(model, *field_names, cascade=True)
    > migrator.rename_field(model, old_field_name, new_field_name)
    > migrator.rename_table(model, new_table_name)
    > migrator.add_index(model, *col_names, unique=False)
    > migrator.drop_index(model, *col_names)
    > migrator.add_not_null(model, *field_names)
    > migrator.drop_not_null(model, *field_names)
    > migrator.add_default(model, field_name, default)

"""

import datetime as dt
import peewee as pw
from peewee_migrate import Migrator
from decimal import ROUND_HALF_EVEN

try:
    import playhouse.postgres_ext as pw_pext
except ImportError:
    pass

SQL = pw.SQL


def migrate(migrator: Migrator, database, fake=False, **kwargs):
    """Write your migrations here."""

    @migrator.create_model
    class BaseModel(pw.Model):
        id = pw.AutoField()

        class Meta:
            table_name = "basemodel"

    @migrator.create_model
    class Day(pw.Model):
        id = pw.IntegerField(primary_key=True)
        subjects = pw.CharField(constraints=[SQL("DEFAULT ''")], default='', max_length=255)

        class Meta:
            table_name = "days"

    @migrator.create_model
    class Subject(pw.Model):
        name = pw.CharField(max_length=255)
        audience = pw.CharField(max_length=255)
        teacher = pw.CharField(max_length=255)
        info = pw.TextField(null=True)

        class Meta:
            table_name = "subjects"

    @migrator.create_model
    class Task(pw.Model):
        text = pw.CharField(max_length=255)
        subject = pw.ForeignKeyField(backref='task_set', column_name='subject_id', field='id', model=migrator.orm['subjects'], null=True)
        date = pw.DateTimeField()

        class Meta:
            table_name = "tasks"

    @migrator.create_model
    class File(pw.Model):
        name = pw.CharField(max_length=255)
        file_id = pw.CharField(max_length=255)
        subject = pw.ForeignKeyField(backref='files', column_name='subject_id', field='id', model=migrator.orm['subjects'], null=True)
        task = pw.ForeignKeyField(backref='files', column_name='task_id', field='id', model=migrator.orm['tasks'], null=True)

        class Meta:
            table_name = "files"

    @migrator.create_model
    class User(pw.Model):
        name = pw.CharField(max_length=255)
        username = pw.CharField(max_length=255)
        photo = pw.CharField(max_length=255, null=True)
        status = pw.CharField(constraints=[SQL("DEFAULT 'user'")], default='user', max_length=255)

        class Meta:
            table_name = "users"



def rollback(migrator: Migrator, database, fake=False, **kwargs):
    """Write your rollback migrations here."""

    migrator.remove_model('users')

    migrator.remove_model('tasks')

    migrator.remove_model('subjects')

    migrator.remove_model('files')

    migrator.remove_model('days')

    migrator.remove_model('basemodel')
