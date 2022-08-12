from peewee import SqliteDatabase, PostgresqlDatabase
from data.config import DB_PORT, DB_PASS, DB_USER, DB_HOST, DB_NAME

if DB_USER and DB_PASS and DB_HOST and DB_PORT and DB_NAME:
    database = PostgresqlDatabase(DB_NAME, user=DB_USER, password=DB_PASS,
                                  host=DB_HOST, port=DB_PORT)
else:
    database = SqliteDatabase(f'data/database.sqlite3')
