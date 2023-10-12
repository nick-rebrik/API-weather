import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeatherInfoApp.settings')

app = Celery('weather')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_connection_retry_on_startup = True

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'collect_weather_data_every_hour': {
        'task': 'apps.weather.tasks.collect_weather_data',
        'schedule': crontab(minute='0', hour='*')
    }
}
