from pathlib import Path
from peewee import SqliteDatabase, PostgresqlDatabase
from . import DB_HOST, DB_NAME, DB_PORT, DB_USER, DB_PASSWORD

database = SqliteDatabase(f"{Path(__file__).absolute().parent.parent}/data/database.sqlite")

if DB_HOST and DB_NAME and DB_PORT and DB_USER and DB_PASSWORD:
    database = PostgresqlDatabase(DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)