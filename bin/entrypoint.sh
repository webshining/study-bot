#!/bin/sh

sleep 5

pw_migrate migrate --database $(python _get_database_url.py) --directory ./migrations

python main.py