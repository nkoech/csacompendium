from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.soils.api.soil.soilserializers import soil_serializers
from csacompendium.soils.models import SoilType
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

soil_serializers = soil_serializers()


def soil_type_serializers():
    """
    Soil type serializers
    :return: All soil type serializers
    :rtype: Object
    """

    class SoilTypeBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """

        class Meta:
            model = SoilType
            fields = [
                'id',
                'soil_type',
                'classification',
            ]

    class SoilTypeRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        soil_properties = SerializerMethodField()

        class Meta:
            model = SoilType
            fields = [
                'soil_properties',
            ]

    class SoilTypeFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_soil_properties(self, obj):
            """
            :param obj: Current record object
            :return: Soil properties of a soil type
            :rtype: Object/record
            """
            request = self.context['request']
            SoilListSerializer = soil_serializers['SoilListSerializer']
            related_content = get_related_content(obj, SoilListSerializer, obj.soil_relation, request)
            return related_content

    class SoilTypeListSerializer(
        SoilTypeBaseSerializer,
        SoilTypeRelationBaseSerializer,
        SoilTypeFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('soil_api:soil_type_detail', 'slug')

        class Meta:
            model = SoilType
            fields = SoilTypeBaseSerializer.Meta.fields + ['url', ] + \
                     SoilTypeRelationBaseSerializer.Meta.fields

    class SoilTypeDetailSerializer(
        SoilTypeBaseSerializer, SoilTypeRelationBaseSerializer,
        FieldMethodSerializer, SoilTypeFieldMethodSerializer
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
            ] + SoilTypeRelationBaseSerializer.Meta.fields
            model = SoilType
            fields = SoilTypeBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'SoilTypeListSerializer': SoilTypeListSerializer,
        'SoilTypeDetailSerializer': SoilTypeDetailSerializer
    }
