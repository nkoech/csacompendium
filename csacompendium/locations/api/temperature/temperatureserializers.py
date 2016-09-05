from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
# from csacompendium.locations.api.serializers import LocationListSerializer
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
        # url = hyperlinked_identity('location_api:temperature_detail', 'pk')

        class Meta:
            model = Temperature
            fields = [
                'temperature',
                'temperature_uom',
                # 'url',
            ]

    return TemperatureListSerializer
