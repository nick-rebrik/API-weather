from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.weather.models import Location
from apps.weather.permisions import XToken
from apps.weather.serializers import LocationSerializer, WeatherDataSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    # permission_classes = (XToken,)


class WeatherDataView(APIView):
    permission_classes = (XToken,)

    def get(self, request, *args, **kwargs):
        day = request.GET.get('day')
        location = request.GET.get('location')

        if not day:
            return Response(
                {'error': 'Parameter "day" is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            day = datetime.strptime(day, '%Y-%m-%d').day
        except ValueError:
            return Response(
                {'error': 'Invalid format for the "day" field. Use the format Y-m-d.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if location:
            try:
                location = Location.objects.get(name=location)
            except Location.DoesNotExist:
                Response(
                    {'error': f'Could not find the location "{location}".'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            try:
                location = Location.objects.get(is_main=True)
            except Location.DoesNotExist:
                Response(
                    {'error': 'No primary location specified.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        weather_data = location.weather_data.filter(created_at__day=day)
        serializer = WeatherDataSerializer(weather_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
