from config import DB_HOST, DB_NAME, DB_PORT, DB_USER, DB_PASSWORD

database = 'sqlite:///data/database.sqlite3'

if DB_HOST and DB_NAME and DB_PORT and DB_USER and DB_PASSWORD:
    database = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


print(database)
