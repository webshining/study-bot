DATABASE_URL := $(shell python _get_database_url.py)
MIGRATIONS_PATH := ./data/migrations


run:
	python app.py
pw_create:
	pw_migrate create --auto --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH} migrate
pw_migrate:
	pw_migrate migrate --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH}
compose:
	docker-compose up -d
logs: 
	docker-compose logs app
rebuild: 
	docker-compose up -d --build --no-deps --force-recreate