from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.soils.api.soil.soilserializers import soil_serializers
from csacompendium.soils.models import SoilTexture
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity


def soil_texture_serializers():
    """
    Soil texture serializers
    :return: All soil texture serializers
    :rtype: Object
    """

    class SoilTextureListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('soil_api:soil_texture_detail', 'slug')

        class Meta:
            model = SoilTexture
            fields = [
                'soil_texture',
                'url',
            ]

    class SoilTextureDetailSerializer(ModelSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        soil_serializers = soil_serializers()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        soil_properties = SerializerMethodField()

        class Meta:
            common_fields = [
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'soil_properties',
            ]
            model = SoilTexture
            fields = [
                'id',
                'soil_texture',
            ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_user(self, obj):
            """
            :param obj: Current record object
            :return: Name of user who created the record
            :rtype: String
            """
            return str(obj.user.username)

        def get_modified_by(self, obj):
            """
            :param obj: Current record object
            :return: Name of user who edited a record
            :rtype: String
            """
            return str(obj.modified_by.username)

        def get_soil_properties(self, obj):
            """
            :param obj: Current record object
            :return: Soil properties of a soil type
            :rtype: Object/record
            """
            request = self.context['request']
            SoilListSerializer = self.soil_serializers['SoilListSerializer']
            try:
                soil_properties = SoilListSerializer(
                    obj.model_type_relation,
                    context={'request': request},
                    many=True
                ).data
                return soil_properties
            except obj.DoesNotExist:
                return None

    return {
        'SoilTextureListSerializer': SoilTextureListSerializer,
        'SoilTextureDetailSerializer': SoilTextureDetailSerializer
    }
