"""Peewee migrations -- 001_migrate.py.

Some examples (model - class or model name)::

    > Model = migrator.orm['table_name']            # Return model in current state by name
    > Model = migrator.ModelClass                   # Return model in current state by name

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
    > migrator.add_not_null(model, *field_names)
    > migrator.add_default(model, field_name, default)
    > migrator.add_constraint(model, name, sql)
    > migrator.drop_index(model, *col_names)
    > migrator.drop_not_null(model, *field_names)
    > migrator.drop_constraints(model, *constraints)

"""

from contextlib import suppress

import peewee as pw
from peewee_migrate import Migrator


with suppress(ImportError):
    import playhouse.postgres_ext as pw_pext


def migrate(migrator: Migrator, database: pw.Database, *, fake=False):
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
        day = pw.ForeignKeyField(column_name='day_id', field='id', model=migrator.orm['days'], on_delete='CASCADE')
        subject = pw.ForeignKeyField(column_name='subject_id', field='id', model=migrator.orm['subjects'], on_delete='CASCADE')
        time_start = pw.TimeField()
        time_end = pw.TimeField()
        group = pw.CharField(max_length=255, null=True)

        class Meta:
            table_name = "days_subjects"

    @migrator.create_model
    class User(pw.Model):
        name = pw.CharField(max_length=255)
        username = pw.CharField(max_length=255, null=True)
        status = pw.CharField(default='user', max_length=255)

        class Meta:
            table_name = "users"


def rollback(migrator: Migrator, database: pw.Database, *, fake=False):
    """Write your rollback migrations here."""
    
    migrator.remove_model('users')

    migrator.remove_model('subjects')

    migrator.remove_model('days_subjects')

    migrator.remove_model('days')

    migrator.remove_model('basemodel')
