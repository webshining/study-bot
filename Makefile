LOCALES_PATH := ./data/locales
LOCALES_DOMAIN := bot

run:
	./bin/entrypoint.sh
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