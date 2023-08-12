#!/bin/sh

pw_migrate migrate --database $(python _get_database_url.py) --directory ./data/migrations

python server.py &
python main.py