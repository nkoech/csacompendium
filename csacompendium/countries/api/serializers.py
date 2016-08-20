from rest_framework.serializers import ModelSerializer
from csacompendium.countries.models import Country


class CountrySerializer(ModelSerializer):
    """
    Country API serializer. Serializes field inputs into an API.
    """
    class Meta:
        model = Country
        fields = [
            'id',
            'country_code',
            'country_name',
            'slug',
        ]
