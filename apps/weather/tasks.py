import logging

from WeatherInfoApp.celery import app
from apps.weather.models import Location, WeatherData
from apps.weather.services.openweather import openweather


@app.task
def collect_weather_data():
    locations = Location.objects.only('pk', 'name')

    for location in locations:
        temperature = openweather.get_weather_data(
            latitude=location.latitude,
            longitude=location.longitude
        )

        WeatherData.objects.create(location=location, temperature=temperature)

        logging.info(f'Weather data for {location.name} collected!')
