from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.locations.api.locationrelation.locationrelationserializer import location_relation_serializers
from csacompendium.locations.models import Temperature
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity


def temperature_serializers():
    """
    Temperature serializers
    :return: All temperature serializers
    :rtype: Object
    """

    class TemperatureListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('location_api:temperature_detail', 'pk')

        class Meta:
            model = Temperature
            fields = [
                'id',
                'temperature',
                'temperature_uom',
                'url',
            ]

    class TemperatureDetailSerializer(ModelSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        create_location_relation_serializer, LocationRelationListSerializer, \
        LocationRelationSerializer, LocationRelationContentTypeSerializer, \
        LocationRelationDetailSerializer = location_relation_serializers()

        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        locations = SerializerMethodField()

        class Meta:
            model = Temperature
            fields = [
                'id',
                'temperature',
                'temperature_uom',
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'locations',
            ]
            read_only_fields = [
                'id',
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'locations',
            ]

        def get_user(self, obj):
            """
            :param obj: Current record object
            :return: Name of user who created the record
            :rtype: String
            """
            return str(obj.user.username)

        def get_modified_by(self, obj):
            """
            :param obj: Current record object
            :return: Name of user who edited a record
            :rtype: String
            """
            return str(obj.modified_by.username)

        def get_locations(self, obj):
            """
            :param obj: Current record object
            :return: Locations in a country
            :rtype: Object/record
            """
            request = self.context['request']
            try:
                locations = self.LocationRelationSerializer(
                    obj.location_relations,
                    context={'request': request},
                    many=True
                ).data
                return locations
            except obj.DoesNotExist:
                return None

    return TemperatureListSerializer, TemperatureDetailSerializer
