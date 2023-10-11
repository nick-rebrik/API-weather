from rest_framework import serializers

from apps.weather.models import Location, WeatherData


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name',)
        read_only_fields = ('latitude', 'longitude', 'is_main')


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ('temperature', 'created_at')
