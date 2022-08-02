DATABASE_URL := $(shell python get_database_url.py)
MIGRATIONS_PATH := ./data/migrations
LOCALES_PATH := ./data/locales

db_revision:
	pw_migrate create --auto --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH} migrate
	# pw_migrate create --auto --database $(python get_database_url.py) --directory ./data/migrations migrate
db_upgrade:
	pw_migrate migrate --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH}
	# pw_migrate migrate --database $(python get_database_url.py) --directory ./data/migrations
pybabel_extract:
	pybabel extract --input-dirs=. -o ${LOCALES_PATH}/bot.pot
	# pybabel extract --input-dirs=. -o ./data/locales/bot.pot
pybabel_compile:
	pybabel compile -d ${LOCALES_PATH} -D bot
	# pybabel compile -d ./data/locales -D bot
pybabel_init:
	pybabel init -i ${LOCALES_PATH}/bot.pot -d ${LOCALES_PATH} -D bot -l en
	pybabel init -i ${LOCALES_PATH}/bot.pot -d ${LOCALES_PATH} -D bot -l ru
	pybabel init -i ${LOCALES_PATH}/bot.pot -d ${LOCALES_PATH} -D bot -l uk
	# pybabel init -i ./data/locales/bot.pot -d ./data/locales -D bot -l en
	# pybabel init -i ./data/locales/bot.pot -d ./data/locales -D bot -l ru
	# pybabel init -i ./data/locales/bot.pot -d ./data/locales -D bot -l uk
pybabel_update:
	pybabel update -d ${LOCALES_PATH} -D bot -i ${LOCALES_PATH}/bot.pot
	# pybabel update -d ./data/locales -D bot -i ./data/locales/bot.pot
