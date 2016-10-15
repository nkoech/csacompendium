from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.locations.api.serializers import location_serializers
from csacompendium.countries.models import Country
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content


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


class CountryDetailSerializer(ModelSerializer, FieldMethodSerializer):
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

    def get_locations(self, obj):
        """
        :param obj: Current record object
        :return: Locations in a country
        :rtype: Object/record
        """
        request = self.context['request']
        LocationListSerializer = location_serializers['LocationListSerializer']
        related_content = get_related_content(obj, LocationListSerializer, obj.locations, request)
        return related_content
