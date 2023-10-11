from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/weather/', include('apps.weather.urls')),
    path('admin/', admin.site.urls),
]
