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
        day_id = pw.IntegerField()

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
    class DaySubject(pw.Model):
        id = pw.AutoField()
        day = pw.ForeignKeyField(backref='subjects', column_name='day_id', field='id', model=migrator.orm['days'], on_delete='CASCADE')
        subject = pw.ForeignKeyField(backref='days', column_name='subject_id', field='id', model=migrator.orm['subjects'], on_delete='CASCADE')
        time_start = pw.TimeField()
        time_end = pw.TimeField()

        class Meta:
            table_name = "days_subjects"

    @migrator.create_model
    class List(pw.Model):
        name = pw.CharField(max_length=255)
        visible = pw.BooleanField(constraints=[SQL("DEFAULT True")], default=True)

        class Meta:
            table_name = "lists"

    @migrator.create_model
    class ListElement(pw.Model):
        list_id = pw.ForeignKeyField(backref='elements', column_name='list_id', field='id', model=migrator.orm['lists'], on_delete='CASCADE')
        key = pw.CharField(max_length=255)
        value = pw.CharField(max_length=255)
        user_id = pw.IntegerField()

        class Meta:
            table_name = "lists_elements"



def rollback(migrator: Migrator, database, fake=False, **kwargs):
    """Write your rollback migrations here."""

    migrator.remove_model('subjects')

    migrator.remove_model('lists_elements')

    migrator.remove_model('lists')

    migrator.remove_model('days_subjects')

    migrator.remove_model('days')

    migrator.remove_model('basemodel')
