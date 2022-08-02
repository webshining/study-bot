from data.config import DB_PASS, DB_NAME, DB_HOST, DB_PORT, DB_USER

DATABASE_URI = f'sqlite:///data/database.sqlite'

if DB_USER and DB_PASS and DB_HOST and DB_PORT and DB_NAME:
    DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

print(DATABASE_URI)
