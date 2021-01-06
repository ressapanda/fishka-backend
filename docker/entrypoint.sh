#!/bin/sh
/app/docker/wait-for-it.sh fishka-db:5432 -t 15 -- echo "PSQL (fishka-db) is up!"

python manage.py migrate
python manage.py loaddata user categories questions

python manage.py collectstatic --noinput --clear

gunicorn -w 4 -b 0.0.0.0:8000 --reload fishka_backend.asgi:application -k uvicorn.workers.UvicornWorker
