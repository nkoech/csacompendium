from .location.locationserializers import location_serializers
from .locationrelation.locationrelationserializer import location_relation_serializers
from .temperature.temperatureserializers import temperature_serializers
from .precipitation.precipitationserializers import precipitation_serializers


location_serializers = location_serializers()
location_relation_serializers = location_relation_serializers()
temperature_serializers = temperature_serializers()
precipitation_serializers = precipitation_serializers()
