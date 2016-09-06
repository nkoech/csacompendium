from .location.locationserializers import location_serializers
from .locationrelation.locationrelationserializer import location_relation_serializers
from .temperature.temperatureserializers import temperature_serializers


# Location serializers
create_location_serializer, LocationListSerializer, LocationDetailSerializer = location_serializers()

# Location relation serializers
LocationRelationListSerializer, LocationRelationContentTypeListSerializer, \
LocationRelationDetailSerializer = location_relation_serializers()

# Temperature serializers
TemperatureListSerializer, TemperatureDetailSerializer = temperature_serializers()
