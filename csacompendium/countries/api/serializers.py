from rest_framework.serializers import ModelSerializer
from csacompendium.countries.models import Country


class CountryListSerializer(ModelSerializer):
    """
    Serialize all records in given fields into an API
    """
    class Meta:
        model = Country
        fields = [
            'id',
            'country_name',
            'slug',
            'country_code',
        ]


class CountryDetailSerializer(ModelSerializer):
    """
    Serialize single record into an API. This is dependent on fields given.
    """
    class Meta:
        model = Country
        fields = [
            'id',
            'country_code',
            'country_name',
            'slug',
            'last_update',
            'time_created',
        ]
