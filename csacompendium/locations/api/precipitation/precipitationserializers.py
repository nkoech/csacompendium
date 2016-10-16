from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.locations.api.locationrelation.locationrelationserializer import location_relation_serializers
from csacompendium.locations.models import Precipitation
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content


def precipitation_serializers():
    """
    Precipitation serializers
    :return: All precipitation serializers
    :rtype: Object
    """

    class PrecipitationListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('location_api:precipitation_detail', 'pk')

        class Meta:
            model = Precipitation
            fields = [
                'id',
                'precipitation',
                'precipitation_uom',
                'precipitation_desc',
                'url',
            ]

    class PrecipitationDetailSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        location_relation_serializers = location_relation_serializers()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        locations = SerializerMethodField()

        class Meta:
            common_fields = [
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'locations',
            ]
            model = Precipitation
            fields = [
                'id',
                'precipitation',
                'precipitation_uom',
                'precipitation_desc',
            ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_locations(self, obj):
            """
            :param obj: Current record object
            :return: Related location relation object
            :rtype: Object/record
            """
            request = self.context['request']
            LocationRelationSerializer = self.location_relation_serializers['LocationRelationSerializer']
            related_content = get_related_content(obj, LocationRelationSerializer, obj.location_relations, request)
            return related_content

    return {
        'PrecipitationListSerializer': PrecipitationListSerializer,
        'PrecipitationDetailSerializer': PrecipitationDetailSerializer
    }
