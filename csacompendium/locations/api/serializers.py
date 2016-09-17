from .location.locationserializers import location_serializers
from .locationrelation.locationrelationserializer import location_relation_serializers
from .temperature.temperatureserializers import temperature_serializers


# Location serializers
location_serializers = location_serializers()

# Location relation serializers
location_relation_serializers = location_relation_serializers()

# Temperature serializers
temperature_serializers = temperature_serializers()
