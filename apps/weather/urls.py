from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.weather import views


app_name = 'weather'

router = DefaultRouter()
router.register('locations', views.LocationViewSet, basename='locations')

urlpatterns = [
    path('', include(router.urls)),
    path('data-by-day/', views.WeatherDataView.as_view(), name='data-by-day')
]