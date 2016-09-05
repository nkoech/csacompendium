from .location.locationviews import location_views
from .temperature.temperatureviews import temperature_views
LocationCreateAPIView, LocationListAPIView, LocationDetailAPIView = location_views()
TemperatureListAPIView = temperature_views()
