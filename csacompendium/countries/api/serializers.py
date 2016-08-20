from rest_framework.serializers import ModelSerializer
from csacompendium.countries.models import Country


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = [
            'id',
            'country_code',
            'country_name',
            'slug',
        ]
