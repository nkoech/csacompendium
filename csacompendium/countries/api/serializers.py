from rest_framework.serializers import ModelSerializer
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
            'url',
            'country_name',
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
            'user',
            'modified_by',
            'last_update',
            'time_created',
        ]


class CountryCreateUpdateSerializer(ModelSerializer):
    """
    Creates or updates a record.
    """
    class Meta:
        model = Country
        fields = [
            'country_code',
            'country_name',
        ]

