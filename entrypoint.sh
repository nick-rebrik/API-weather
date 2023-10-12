#!/bin/sh

dockerize -wait tcp://db:5432 -timeout 1m

python manage.py migrate
python manage.py collectstatic --noinput

python manage.py create_default_location

gunicorn WeatherInfoApp.wsgi:application --bind 0.0.0.0:8000

exec "$@"
