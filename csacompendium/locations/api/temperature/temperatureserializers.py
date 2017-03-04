from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.locations.api.locationrelation.locationrelationserializer import location_relation_serializers
from csacompendium.locations.models import Temperature
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

location_relation_serializers = location_relation_serializers()

def temperature_serializers():
    """
    Temperature serializers
    :return: All temperature serializers
    :rtype: Object
    """

    class TemperatureBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = Temperature
            fields = [
                'id',
                'temperature',
                'temperature_uom',
            ]

    class TemperatureRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        locations = SerializerMethodField()

        class Meta:
            model = Temperature
            fields = [
                'locations',
            ]

    class TemperatureFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_locations(self, obj):
            """
            :param obj: Current record object
            :return: Locations related to the temperature
            :rtype: Object/record
            """
            request = self.context['request']
            LocationRelationSerializer = location_relation_serializers['LocationRelationSerializer']
            related_content = get_related_content(obj, LocationRelationSerializer, obj.location_relations, request)
            return related_content

    class TemperatureListSerializer(
        TemperatureBaseSerializer,
        TemperatureRelationBaseSerializer,
        TemperatureFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('location_api:temperature_detail', 'pk')

        class Meta:
            model = Temperature
            fields = TemperatureBaseSerializer.Meta.fields + ['url', ] + \
                     TemperatureRelationBaseSerializer.Meta.fields

    class TemperatureDetailSerializer(
        TemperatureBaseSerializer, TemperatureRelationBaseSerializer,
        FieldMethodSerializer, TemperatureFieldMethodSerializer
    ):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        user = SerializerMethodField()
        modified_by = SerializerMethodField()

        class Meta:
            common_fields = [
                'user',
                'modified_by',
                'last_update',
                'time_created',
            ] + TemperatureRelationBaseSerializer.Meta.fields
            model = Temperature
            fields = TemperatureBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'TemperatureListSerializer': TemperatureListSerializer,
        'TemperatureDetailSerializer': TemperatureDetailSerializer
    }
