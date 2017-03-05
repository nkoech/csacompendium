from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.soils.api.soil.soilserializers import soil_serializers
from csacompendium.soils.models import SoilTexture
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

soil_serializers = soil_serializers()


def soil_texture_serializers():
    """
    Soil texture serializers
    :return: All soil texture serializers
    :rtype: Object
    """

    class SoilTextureBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = SoilTexture
            fields = [
                'id',
                'soil_texture',
            ]

    class SoilTextureRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        soil_properties = SerializerMethodField()

        class Meta:
            model = SoilTexture
            fields = [
                'soil_properties',
            ]

    class SoilTextureFieldMethodSerializer:
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

    class SoilTextureListSerializer(
        SoilTextureBaseSerializer,
        SoilTextureRelationBaseSerializer,
        SoilTextureFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('soil_api:soil_texture_detail', 'slug')

        class Meta:
            model = SoilTexture
            fields = SoilTextureBaseSerializer.Meta.fields + ['url', ] + \
                     SoilTextureRelationBaseSerializer.Meta.fields

    class SoilTextureDetailSerializer(
        SoilTextureBaseSerializer, SoilTextureRelationBaseSerializer,
        FieldMethodSerializer, SoilTextureFieldMethodSerializer
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
            ] + SoilTextureRelationBaseSerializer.Meta.fields
            model = SoilTexture
            fields = SoilTextureBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'SoilTextureListSerializer': SoilTextureListSerializer,
        'SoilTextureDetailSerializer': SoilTextureDetailSerializer
    }
