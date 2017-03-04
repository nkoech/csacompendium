from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.locations.api.locationrelation.locationrelationserializer import location_relation_serializers
from csacompendium.locations.models import Precipitation
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

location_relation_serializers = location_relation_serializers()


def precipitation_serializers():
    """
    Precipitation serializers
    :return: All precipitation serializers
    :rtype: Object
    """

    class PrecipitationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = Precipitation
            fields = [
                'id',
                'precipitation',
                'precipitation_uom',
                'precipitation_desc',
            ]

    class PrecipitationRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        locations = SerializerMethodField()

        class Meta:
            model = Precipitation
            fields = [
                'locations',
            ]

    class PrecipitationFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_locations(self, obj):
            """
            :param obj: Current record object
            :return: Related location relation object
            :rtype: Object/record
            """
            request = self.context['request']
            LocationRelationSerializer = location_relation_serializers['LocationRelationSerializer']
            related_content = get_related_content(obj, LocationRelationSerializer, obj.location_relations, request)
            return related_content

    class PrecipitationListSerializer(
        PrecipitationBaseSerializer,
        PrecipitationRelationBaseSerializer,
        PrecipitationFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('location_api:precipitation_detail', 'pk')

        class Meta:
            model = Precipitation
            fields = PrecipitationBaseSerializer.Meta.fields + ['url', ] + \
                     PrecipitationRelationBaseSerializer.Meta.fields

    class PrecipitationDetailSerializer(
        PrecipitationBaseSerializer,
        PrecipitationRelationBaseSerializer,
        FieldMethodSerializer,
        PrecipitationFieldMethodSerializer
    ):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        user = SerializerMethodField()
        modified_by = SerializerMethodField()

        class Meta:
            common_fields = [
                'user',
                'modified_by',
                'last_update',
                'time_created',
            ] + PrecipitationRelationBaseSerializer.Meta.fields
            model = Precipitation
            fields = PrecipitationBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'PrecipitationListSerializer': PrecipitationListSerializer,
        'PrecipitationDetailSerializer': PrecipitationDetailSerializer
    }
