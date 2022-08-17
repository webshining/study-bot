MIGRATIONS_PATH := ./data/migrations
DATABASE_URL := $(shell python _get_db_url.py)


db_revision:
	pw_migrate create --auto --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH} migrate
db_migrate:
	pw_migrate migrate --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH}
db_rollback:
	pw_migrate rollback --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH} --count 1
