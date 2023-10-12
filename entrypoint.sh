#!/bin/sh

set -o allexport
source .env
set +o allexport

dockerize -wait tcp://db:5432 -timeout 1m

while ! python -c "import psycopg2; psycopg2.connect(host='$DB_HOST', dbname='$DB_NAME', user='$DB_USER', password='$DB_PASSWORD')" 2>/dev/null
do
  echo "The database is not yet available. Waiting..."
  sleep 5
done

python manage.py migrate
python manage.py collectstatic --noinput

python manage.py create_default_location

gunicorn WeatherInfoApp.wsgi:application --bind 0.0.0.0:8000

exec "$@"
