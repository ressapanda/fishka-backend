#!/bin/bash

python manage.py migrate
python manage.py loaddata user categories questions

python manage.py collectstatic --noinput --clear

gunicorn -w 4 -b 0.0.0.0:8000 --reload fishka_backend.wsgi:application
