from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.locations.api.location.locationserializers import location_serializers
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
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        # create_location_serializer, LocationListSerializer, LocationDetailSerializer = location_serializers()
        # locations = SerializerMethodField()

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
                # 'locations',
            ]
            read_only_fields = [
                'id',
                'user',
                'modified_by',
                'last_update',
                'time_created',
                # 'locations',
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

        # def get_locations(self, obj):
        #     """
        #     :param obj: Current record object
        #     :return: Locations in a country
        #     :rtype: Object/record
        #     """
        #     request = self.context['request']
        #     locations = LocationListSerializer(obj.locations, context={'request': request}, many=True).data
        #     if not locations:
        #         return None
        #     return locations

    return TemperatureListSerializer, TemperatureDetailSerializer
