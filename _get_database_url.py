from data.config import DIR, DB_HOST, DB_PASS, DB_PORT, DB_USER, DB_NAME

database = f'sqlite:///{DIR}/data/database.sqlite3'
if DB_NAME and DB_USER and DB_PASS and DB_HOST and DB_PORT:
    database = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


if __name__ == "__main__":
    print(database)
