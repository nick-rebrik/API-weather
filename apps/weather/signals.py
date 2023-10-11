import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.weather.models import Location
from apps.weather.services.openweather import openweather, OpenWeatherError


@receiver(post_save, sender=Location)
def add_coordinates(instance, **kwargs):
    if kwargs['created']:
        try:
            latitude, longitude = openweather.get_coordinates_by_location(instance.name)
            instance.latitude = latitude
            instance.longitude = longitude
            instance.save()

        except OpenWeatherError as e:
            logging.error(e)
