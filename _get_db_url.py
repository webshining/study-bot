from data.config import DB_HOST, DB_PASS, DB_USER, DB_PORT, DB_NAME

DATABASE_URI = f'sqlite:///data/database.sqlite3'

if DB_USER and DB_PASS and DB_HOST and DB_PORT and DB_NAME:
    DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

print(DATABASE_URI)
