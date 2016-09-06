from .location.locationviews import location_views
from .locationrelation.locationrelationviews import location_relation_views
from .temperature.temperatureviews import temperature_views
LocationCreateAPIView, LocationListAPIView, LocationDetailAPIView = location_views()
LocationRelationListAPIView = location_relation_views()
TemperatureListAPIView, TemperatureDetailAPIView, TemperatureCreateAPIView = temperature_views()
