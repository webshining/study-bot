MIGRATIONS_PATH := ./migrations
DATABASE_URL := $(shell python db_url.pi)

db_init:
	pw_migrate create --auto --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH} migrate
db_migrate:
	pw_migrate migrate --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH}