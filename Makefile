DATABASE_URL ?= $(shell python _get_database_url.py)
MIGRATIONS_PATH := ./migrations
LOCALES_PATH := ./data/locales
LOCALES_DOMAIN := bot


run:
	python main.py
pw_create:
	pw_migrate create --auto --auto-source database.models --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH} migrate
pw_migrate:
	pw_migrate migrate --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH}
pw_rollback:
	pw_migrate rollback --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH} --count 1
pybabel_extract: 
	pybabel extract --input-dirs=. -o $(LOCALES_PATH)/$(LOCALES_DOMAIN).pot
pybabel_init: 
	pybabel init -i $(LOCALES_PATH)/$(LOCALES_DOMAIN).pot -d $(LOCALES_PATH) -D $(LOCALES_DOMAIN) -l en && \
	pybabel init -i $(LOCALES_PATH)/$(LOCALES_DOMAIN).pot -d $(LOCALES_PATH) -D $(LOCALES_DOMAIN) -l ru && \
	pybabel init -i $(LOCALES_PATH)/$(LOCALES_DOMAIN).pot -d $(LOCALES_PATH) -D $(LOCALES_DOMAIN) -l uk
pybabel_update: 
	pybabel update -i $(LOCALES_PATH)/$(LOCALES_DOMAIN).pot -d ./data/locales -D $(LOCALES_DOMAIN)
pybabel_compile: 
	pybabel compile -d $(LOCALES_PATH) -D $(LOCALES_DOMAIN)
compose:
	docker-compose up -d
logs: 
	docker-compose logs app
rebuild: 
	docker-compose up -d --no-deps --force-recreate --build