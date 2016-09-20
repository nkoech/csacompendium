# from csacompendium.soils.api.locationrelation.locationrelationserializer import location_relation_serializers
from csacompendium.soils.models import Soil
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import CreateSerializerUtil
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)


def soil_serializers():
    """
    Soil serializers
    :return: All location serializers
    :rtype: Object
    """

    class SoilBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = Soil
            fields = [
                'som',
                'som_uom',
                'initial_soc',
                'soil_ph',
                'soil_years',
            ]

    class SoilListSerializer(SoilBaseSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('soil_api:soil_detail', 'pk')

        class Meta:
            model = Soil
            fields = SoilBaseSerializer.Meta.fields + ['url', ]

    class SoilDetailSerializer(SoilBaseSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        # location_relation_serializers = location_relation_serializers()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        content_type_url = SerializerMethodField()
        # relation_details = SerializerMethodField()

        class Meta:
            common_fields = [
                'modified_by',
                'last_update',
                'time_created',
                'content_type_url',
                # 'relation_details',
            ]
            model = Soil
            fields = ['id', ] + SoilBaseSerializer.Meta.fields + ['user', ] + common_fields
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

        def get_content_type_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            try:
                return obj.content_object.get_api_url()
            except:
                return None

        # def get_relation_details(self, obj):
        #     """
        #     Get related object type data
        #     :param obj: Current record object
        #     :return: Locations in a country
        #     :rtype: Object/record
        #     """
        #     request = self.context['request']
        #     LocationRelationContentTypeSerializer = self.location_relation_serializers[
        #         'LocationRelationContentTypeSerializer'
        #     ]
        #     try:
        #         content_type = LocationRelationContentTypeSerializer(
        #             obj.model_type_relation,
        #             context={'request': request},
        #             many=True
        #         ).data
        #         return content_type
        #     except obj.DoesNotExist:
        #         return None

    return {
        # 'create_location_serializer': create_location_serializer,
        'SoilListSerializer': SoilListSerializer,
        'SoilDetailSerializer': SoilDetailSerializer
    }
