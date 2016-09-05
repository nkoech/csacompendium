from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.locations.api.serializers import LocationListSerializer
from csacompendium.countries.models import Country
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity


class CountryListSerializer(ModelSerializer):
    """
    Serialize all records in given fields into an API
    """
    url = hyperlinked_identity('country_api:detail', 'slug')

    class Meta:
        model = Country
        fields = [
            'country_name',
            'country_code',
            'url',
        ]


class CountryDetailSerializer(ModelSerializer):
    """
    Serialize single record into an API. This is dependent on fields given.
    """
    user = SerializerMethodField()
    modified_by = SerializerMethodField()
    locations = SerializerMethodField()

    class Meta:
        model = Country
        fields = [
            'id',
            'country_code',
            'country_name',
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
        locations = LocationListSerializer(obj.locations, context={'request': request}, many=True).data
        if not locations:
            return None
        return locations
