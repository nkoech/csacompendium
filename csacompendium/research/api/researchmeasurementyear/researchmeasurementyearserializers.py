from csacompendium.research.models import (
    MeasurementYear,
    MeasurementDuration,
    MeasurementSeason,
    ResearchMeasurementYear,
)
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import (
    CreateSerializerUtil,
    get_related_content_url,
    FieldMethodSerializer
)
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)


def research_measurement_year_serializers():
    """
    Research measurement year serializers
    :return: All research measurement year serializers
    :rtype: Object
    """

    class ResearchMeasurementYearBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = ResearchMeasurementYear
            fields = [
                'id',
                'measurementyear',
                'measurementduration',
                'measurementseason',
            ]

    class ResearchMeasurementYearRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        measurement_year_url = SerializerMethodField()
        measurement_duration_url = SerializerMethodField()
        measurement_season_url = SerializerMethodField()
        content_type_url = SerializerMethodField()

        class Meta:
            model = ResearchMeasurementYear
            fields = [
                'measurement_year_url',
                'content_type_url',
                'measurement_duration_url',
                'measurement_season_url',
            ]

    class ResearchMeasurementYearFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research measurement year id
            :rtype: String
            """
            return obj.id

        def get_measurement_year_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            if obj.measurementyear:
                return get_related_content_url(MeasurementYear, obj.measurementyear.id)

        def get_measurement_duration_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            if obj.measurementduration:
                return get_related_content_url(MeasurementDuration, obj.measurementduration.id)

        def get_measurement_season_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            if obj.measurementseason:
                return get_related_content_url(MeasurementSeason, obj.measurementseason.id)

    def create_research_measurement_year_serializer(model_type=None, pk=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param pk: Primary key
        :param user: Object owner
        :return: Serializer class
        :rtype: Object
        """

        class ResearchMeasurementYearCreateSerializer(
            ResearchMeasurementYearBaseSerializer,
            CreateSerializerUtil
        ):
            """
            Create a record
            """
            class Meta:
                model = ResearchMeasurementYear
                fields = ResearchMeasurementYearBaseSerializer.Meta.fields + ['last_update', 'time_created', ]

            def __init__(self, *args, **kwargs):
                super(ResearchMeasurementYearCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = pk
                self.user = user
                self.slugify = False
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Research measurement year object
                :rtype: Object
                """
                measurementyear = validated_data.get('measurementyear')
                measurementduration = validated_data.get('measurementduration')
                measurementseason = validated_data.get('measurementseason')
                measurement_year_relation = ResearchMeasurementYear.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    measurementyear=measurementyear,
                    measurementduration=measurementduration,
                    measurementseason=measurementseason,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if measurement_year_relation:
                    return measurement_year_relation
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return ResearchMeasurementYearCreateSerializer

    class ResearchMeasurementYearListSerializer(
        ResearchMeasurementYearBaseSerializer, ResearchMeasurementYearRelationBaseSerializer,
        FieldMethodSerializer, ResearchMeasurementYearFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        research_measurement_year_url = hyperlinked_identity(
            'research_api:research_measurement_year_detail', 'pk'
        )

        class Meta:
            model = ResearchMeasurementYear
            fields = ResearchMeasurementYearBaseSerializer.Meta.fields + \
                     ['research_measurement_year_url', ] + \
                     ResearchMeasurementYearRelationBaseSerializer.Meta.fields

    class ResearchMeasurementYearSerializer(
        ModelSerializer,
        ResearchMeasurementYearFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        measurement_year_url = SerializerMethodField()
        relation_id = SerializerMethodField()
        research_measurement_year_url = hyperlinked_identity(
            'research_api:research_measurement_year_detail', 'pk'
        )
        measurement_duration_url = SerializerMethodField()
        measurement_season_url = SerializerMethodField()

        class Meta:
            model = ResearchMeasurementYear
            fields = [
                'relation_id',
                'measurementyear_id',
                'measurement_year_url',
                'research_measurement_year_url',
                'measurement_duration_url',
                'measurement_season_url',
            ]

    class ResearchMeasurementYearContentTypeSerializer(
        ModelSerializer,
        FieldMethodSerializer,
        ResearchMeasurementYearFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        relation_id = SerializerMethodField()
        content_type_url = SerializerMethodField()
        research_measurement_year_url = hyperlinked_identity(
            'research_api:research_measurement_year_detail', 'pk'
        )
        measurement_duration_url = SerializerMethodField()
        measurement_season_url = SerializerMethodField()

        class Meta:
            model = ResearchMeasurementYear
            fields = [
                'relation_id',
                'object_id',
                'content_type_url',
                'research_measurement_year_url',
                'measurement_duration_url',
                'measurement_season_url',
            ]

    class ResearchMeasurementYearDetailSerializer(
        ResearchMeasurementYearBaseSerializer, ResearchMeasurementYearRelationBaseSerializer,
        FieldMethodSerializer, ResearchMeasurementYearFieldMethodSerializer
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
            ] + ResearchMeasurementYearRelationBaseSerializer.Meta.fields
            model = ResearchMeasurementYear
            fields = ResearchMeasurementYearBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'create_research_measurement_year_serializer': create_research_measurement_year_serializer,
        'ResearchMeasurementYearListSerializer': ResearchMeasurementYearListSerializer,
        'ResearchMeasurementYearSerializer': ResearchMeasurementYearSerializer,
        'ResearchMeasurementYearContentTypeSerializer': ResearchMeasurementYearContentTypeSerializer,
        'ResearchMeasurementYearDetailSerializer': ResearchMeasurementYearDetailSerializer
    }
