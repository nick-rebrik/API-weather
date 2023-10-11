import json
import logging
import os

import requests
from dotenv import load_dotenv

logger = logging.getLogger('openweather')

load_dotenv()

API_KEY = os.environ.get('OPEN_WEATHER_API_KEY')


class OpenWeather:
    ROOT_URL = 'https://api.openweathermap.org'

    def get_coordinates_by_location(self, location: str) -> tuple:
        """
        Retrieve latitude and longitude coordinates for a given location using the OpenWeatherMap API.

        :param location: A string representing the location for which coordinates are requested.
        :return: A tuple containing latitude and longitude as floats (latitude, longitude).
        :raises: OpenWeatherError if an error occurs during the API request.
        """

        url = f'{self.ROOT_URL}/geo/1.0/direct'

        params = {
            'q': location,
            'appid': API_KEY,
            'limit': 1
        }

        request = requests.get(url=url, params=params)
        response = request.json()

        if request.status_code == 200:
            response = response[0]
            latitude = response.get('lat')
            longitude = response.get('lon')
            return latitude, longitude

        error_message = response.get('message')
        logger.error(error_message)
        raise OpenWeatherError(error_message)

    def get_weather_data(self, latitude: float, longitude: float, units: str = 'metric'):
        """
        Retrieve weather data for a specific location based on its latitude and longitude using the OpenWeatherMap API.

        :param latitude: A float representing the latitude of the location.
        :param longitude: A float representing the longitude of the location.
        :param units: A string specifying the units for temperature (e.g., 'metric' for Celsius, 'imperial' for Fahrenheit).
        :return: A dictionary containing weather data information.
        :raises: OpenWeatherError if an error occurs during the API request.
        """

        url = f'{self.ROOT_URL}/data/2.5/weather'

        params = {
            'lat': latitude,
            'lon': longitude,
            'units': units,
            'appid': API_KEY,
        }

        request = requests.get(url=url, params=params)
        response = request.json()

        if request.status_code == 200:
            return response

        error_message = response.get('message')
        logger.error(error_message)
        raise OpenWeatherError(error_message)


class OpenWeatherError(BaseException):
    pass


openweather = OpenWeather()
