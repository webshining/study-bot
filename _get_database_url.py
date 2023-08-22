from data.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

database = f'sqlite:///database.sqlite3'
if DB_NAME and DB_USER and DB_PASS and DB_HOST and DB_PORT:
    database = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


if __name__ == "__main__":
    print(database)
