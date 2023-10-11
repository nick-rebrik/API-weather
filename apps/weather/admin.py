from django.contrib import admin

from apps.weather.models import Location, WeatherData


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    ...


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    ...
