from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=225, unique=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    is_main = models.BooleanField(default=False, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class WeatherData(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='weather_data')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.location.name} | {self.created_at}'
