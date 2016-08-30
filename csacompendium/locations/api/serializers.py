from rest_framework.serializers import (
    ModelSerializer, SerializerMethodField
)
from csacompendium.locations.models import Location
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity


class LocationListSerializer(ModelSerializer):
    """
    Serialize all records in given fields into an API
    """
    # url = hyperlinked_identity('location_api:detail', 'slug')

    class Meta:
        model = Location
        fields = [
            'location_name',
            'latitude',
            'longitude',
            'elevation',
        ]


class LocationDetailSerializer(ModelSerializer):
    """
    Serialize single record into an API. This is dependent on fields given.
    """
    user = SerializerMethodField()
    modified_by = SerializerMethodField()

    class Meta:
        model = Location
        fields = [
            'id',
            'object_id',
            'location_name',
            'latitude',
            'longitude',
            'elevation',
            'user',
            'modified_by',
            'last_update',
            'time_created',
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
