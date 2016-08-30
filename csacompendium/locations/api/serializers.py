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
            'elevation'
        ]
