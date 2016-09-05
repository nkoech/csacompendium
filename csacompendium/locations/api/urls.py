from django.conf.urls import url
from .views import (
    LocationCreateAPIView,
    LocationDetailAPIView,
    LocationListAPIView,
    TemperatureListAPIView,
    TemperatureDetailAPIView,
    TemperatureCreateAPIView,
)

#  Location URLs
urlpatterns = [
    url(r'^temperature/$', TemperatureListAPIView.as_view(), name='temperature_list'),
    url(r'^temperature/create/$', TemperatureCreateAPIView.as_view(), name='temperature_create'),
    url(r'^temperature/(?P<pk>[\w-]+)/$', TemperatureDetailAPIView.as_view(), name='temperature_detail'),
    url(r'^$', LocationListAPIView.as_view(), name='location_list'),
    url(r'^create/$', LocationCreateAPIView.as_view(), name='location_create'),
    url(r'^(?P<slug>[\w-]+)/$', LocationDetailAPIView.as_view(), name='location_detail'),
]
