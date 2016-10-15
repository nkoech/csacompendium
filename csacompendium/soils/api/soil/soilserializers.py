from csacompendium.soils.models import (
    Soil,
    SoilType,
    SoilTexture,
)
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import CreateSerializerUtil, FieldMethodSerializer
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)


def soil_serializers():
    """
    Soil serializers
    :return: All soil serializers
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

    def create_soil_serializer(model_type=None, slug=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param slug: slug
        :param user: Record owner
        :return: Serializer class
        :rtype: Object
        """

        class SoilCreateSerializer(SoilBaseSerializer, CreateSerializerUtil):
            """
            Create a record
            """

            class Meta:
                model = Soil
                fields = ['id', 'soiltype', 'soiltexture', ] + \
                         SoilBaseSerializer.Meta.fields + \
                         ['last_update', 'time_created', ]

            def __init__(self, *args, **kwargs):
                super(SoilCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = slug
                self.user = user
                self.slugify = True
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Soil object
                :rtype: Object
                """
                soiltype = validated_data.get('soiltype')
                soiltexture = validated_data.get('soiltexture')
                som = validated_data.get('som')
                som_uom = validated_data.get('som_uom')
                initial_soc = validated_data.get('initial_soc')
                soil_ph = validated_data.get('soil_ph')
                soil_years = validated_data.get('soil_years')
                soil = Soil.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    soiltype=soiltype,
                    soiltexture=soiltexture,
                    som=som,
                    som_uom=som_uom,
                    initial_soc=initial_soc,
                    soil_ph=soil_ph,
                    soil_years=soil_years,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if soil:
                    return soil
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return SoilCreateSerializer

    class SoilListSerializer(SoilBaseSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('soil_api:soil_detail', 'pk')

        class Meta:
            model = Soil
            fields = SoilBaseSerializer.Meta.fields + ['url', ]

    class SoilDetailSerializer(SoilBaseSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        soil_type_url = SerializerMethodField()
        soil_texture_url = SerializerMethodField()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        content_type_url = SerializerMethodField()

        class Meta:
            common_fields = [
                'modified_by',
                'last_update',
                'time_created',
                'content_type_url',
            ]
            model = Soil
            fields = ['id', 'soil_type_url', 'soil_texture_url', ] + \
                     SoilBaseSerializer.Meta.fields + ['user', ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_soil_type_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            try:
                soiltype_obj = SoilType.objects.get(id=obj.soiltype.id)
                return soiltype_obj.get_api_url()
            except:
                return None

        def get_soil_texture_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            try:
                soiltexture_obj = SoilTexture.objects.get(id=obj.soiltexture.id)
                return soiltexture_obj.get_api_url()
            except:
                return None

    return {
        'create_soil_serializer': create_soil_serializer,
        'SoilListSerializer': SoilListSerializer,
        'SoilDetailSerializer': SoilDetailSerializer
    }
