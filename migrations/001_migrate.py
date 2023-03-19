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

import peewee as pw
from peewee_migrate import Migrator
from decimal import ROUND_HALF_EVEN

try:
    import playhouse.postgres_ext as pw_pext
except ImportError:
    pass

SQL = pw.SQL


def migrate(migrator: Migrator, database: pw.Database, fake=False, **kwargs):
    """Write your migrations here."""
    
    @migrator.create_model
    class BaseModel(pw.Model):
        id = pw.AutoField()

        class Meta:
            table_name = "basemodel"

    @migrator.create_model
    class Chat(pw.Model):
        chatId = pw.DecimalField(auto_round=False, decimal_places=5, max_digits=20, rounding=ROUND_HALF_EVEN)
        facultyId = pw.IntegerField()
        courseId = pw.IntegerField()
        groupId = pw.IntegerField()

        class Meta:
            table_name = "chat"



def rollback(migrator: Migrator, database: pw.Database, fake=False, **kwargs):
    """Write your rollback migrations here."""
    
    migrator.remove_model('chat')

    migrator.remove_model('basemodel')
