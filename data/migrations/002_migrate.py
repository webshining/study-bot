"""Peewee migrations -- 002_migrate.py.

Some examples (model - class or model name)::

    > Model = migrator.orm['table_name']            # Return model in current state by name
    > Model = migrator.ModelClass                   # Return model in current state by name

    > migrator.sql(sql)                             # Run custom SQL
    > migrator.run(func, *args, **kwargs)           # Run python function with the given args
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

import datetime
from contextlib import suppress

import peewee as pw
from peewee_migrate import Migrator

with suppress(ImportError):
    import playhouse.postgres_ext as pw_pext


def migrate(migrator: Migrator, database: pw.Database, *, fake=False):
    """Write your migrations here."""
    
    migrator.add_fields(
        'user',

        updated_at=pw.DateField(default=datetime.date(2023, 9, 14)))

    @migrator.create_model
    class Task(pw.Model):
        id = pw.AutoField()
        subject = pw.CharField(max_length=255)
        text = pw.TextField()
        group_id = pw.CharField(max_length=255)
        date = pw.DateField()

        class Meta:
            table_name = "task"

    @migrator.create_model
    class File(pw.Model):
        id = pw.AutoField()
        file_id = pw.CharField(max_length=255)
        file_type = pw.CharField(max_length=255)
        task = pw.ForeignKeyField(column_name='task_id', field='id', model=migrator.orm['task'])

        class Meta:
            table_name = "file"


def rollback(migrator: Migrator, database: pw.Database, *, fake=False):
    """Write your rollback migrations here."""
    
    migrator.remove_fields('user', 'updated_at')

    migrator.remove_model('task')

    migrator.remove_model('file')
