DATABASE_URL := $(shell python get_database_url.py)
MIGRATIONS_PATH := ./data/migrations

db_revision:
	pw_migrate create --auto --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH} migrate
	# pw_migrate create --auto --database $(python get_database_url.py) --directory ./data/migrations migrate
db_upgrade:
	pw_migrate migrate --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH}
	# pw_migrate migrate --database $(python get_database_url.py) --directory ./data/migrations