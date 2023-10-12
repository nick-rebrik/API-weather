from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as yasg_urls

urlpatterns = [
    path('api/weather/', include('apps.weather.urls')),
    path('api/doc/', include(yasg_urls)),
    path('admin/', admin.site.urls),
]
