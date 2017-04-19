from csacompendium.indicators.models import (
    OutcomeIndicator,
    SoilMeasurement,
    ExperimentOutcome,
    ResearchOutcomeIndicator,
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


def research_outcome_indicator_serializers():
    """
    Research outcome indicator serializers
    :return: All research outcome indicator serializers
    :rtype: Object
    """

    class ResearchOutcomeIndicatorBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """

        class Meta:
            model = ResearchOutcomeIndicator
            fields = [
                'id',
                'outcomeindicator',
                'soilmeasurement',
                'experimentoutcome',
            ]

    class ResearchOutcomeIndicatorRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        content_type_url = SerializerMethodField()
        soil_measurement_url = SerializerMethodField()
        experiment_outcome_url = SerializerMethodField()
        outcome_indicator_url = SerializerMethodField()

        class Meta:
            model = ResearchOutcomeIndicator
            fields = [
                'content_type_url',
                'soil_measurement_url',
                'experiment_outcome_url',
                'outcome_indicator_url',
            ]

    class ResearchOutcomeIndicatorFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research outcome indicator id
            :rtype: String
            """
            return obj.id

        def get_outcome_indicator_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            if obj.outcomeindicator:
                return get_related_content_url(OutcomeIndicator, obj.outcomeindicator.id)

        def get_soil_measurement_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            if obj.soilmeasurement:
                return get_related_content_url(SoilMeasurement, obj.soilmeasurement.id)

        def get_experiment_outcome_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            if obj.experimentoutcome:
                return get_related_content_url(ExperimentOutcome, obj.experimentoutcome.id)

    def create_research_outcome_indicator_serializer(model_type=None, pk=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param pk: Primary key
        :param user: Object owner
        :return: Serializer class
        :rtype: Object
        """

        class ResearchOutcomeIndicatorCreateSerializer(
            ResearchOutcomeIndicatorBaseSerializer, CreateSerializerUtil
        ):
            """
            Create a record
            """
            class Meta:
                model = ResearchOutcomeIndicator
                fields = ResearchOutcomeIndicatorBaseSerializer.Meta.fields + ['last_update', 'time_created', ]

            def __init__(self, *args, **kwargs):
                super(ResearchOutcomeIndicatorCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = pk
                self.user = user
                self.slugify = False
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Research outcome indicator object
                :rtype: Object
                """
                outcomeindicator = validated_data.get('outcomeindicator')
                soilmeasurement = validated_data.get('soilmeasurement')
                experimentoutcome = validated_data.get('experimentoutcome')
                outcomeindicator_relation = ResearchOutcomeIndicator.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    outcomeindicator=outcomeindicator,
                    soilmeasurement=soilmeasurement,
                    experimentoutcome=experimentoutcome,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if outcomeindicator_relation:
                    return outcomeindicator_relation
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return ResearchOutcomeIndicatorCreateSerializer

    class ResearchOutcomeIndicatorListSerializer(
        ResearchOutcomeIndicatorBaseSerializer, ResearchOutcomeIndicatorRelationBaseSerializer,
        FieldMethodSerializer, ResearchOutcomeIndicatorFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        research_outcome_indicator_url = hyperlinked_identity(
            'indicator_outcome_api:research_outcome_indicator_detail', 'pk'
        )

        class Meta:
            model = ResearchOutcomeIndicator
            fields = ResearchOutcomeIndicatorBaseSerializer.Meta.fields + \
                     ['research_outcome_indicator_url', ] + \
                     ResearchOutcomeIndicatorRelationBaseSerializer.Meta.fields

    class ResearchOutcomeIndicatorSerializer(ModelSerializer, ResearchOutcomeIndicatorFieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        outcome_indicator_url = SerializerMethodField()
        relation_id = SerializerMethodField()
        research_outcome_indicator_url = hyperlinked_identity(
            'indicator_outcome_api:research_outcome_indicator_detail', 'pk'
        )
        soil_measurement_url = SerializerMethodField()
        experiment_outcome_url = SerializerMethodField()

        class Meta:
            model = ResearchOutcomeIndicator
            fields = [
                'relation_id',
                'outcomeindicator_id',
                'outcome_indicator_url',
                'research_outcome_indicator_url',
                'soil_measurement_url',
                'experiment_outcome_url',
            ]

    class ResearchOutcomeIndicatorContentTypeSerializer(
        ModelSerializer,
        FieldMethodSerializer,
        ResearchOutcomeIndicatorFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        relation_id = SerializerMethodField()
        content_type_url = SerializerMethodField()
        research_outcome_indicator_url = hyperlinked_identity(
            'indicator_outcome_api:research_outcome_indicator_detail', 'pk'
        )
        soil_measurement_url = SerializerMethodField()
        experiment_outcome_url = SerializerMethodField()

        class Meta:
            model = ResearchOutcomeIndicator
            fields = [
                'relation_id',
                'object_id',
                'content_type_url',
                'research_outcome_indicator_url',
                'soil_measurement_url',
                'experiment_outcome_url',
            ]

    class ResearchOutcomeIndicatorDetailSerializer(
        ResearchOutcomeIndicatorBaseSerializer, ResearchOutcomeIndicatorRelationBaseSerializer,
        FieldMethodSerializer, ResearchOutcomeIndicatorFieldMethodSerializer
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
            ] + ResearchOutcomeIndicatorRelationBaseSerializer.Meta.fields
            model = ResearchOutcomeIndicator

            fields = ResearchOutcomeIndicatorBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields

    return {
        'create_research_outcome_indicator_serializer': create_research_outcome_indicator_serializer,
        'ResearchOutcomeIndicatorListSerializer': ResearchOutcomeIndicatorListSerializer,
        'ResearchOutcomeIndicatorSerializer': ResearchOutcomeIndicatorSerializer,
        'ResearchOutcomeIndicatorContentTypeSerializer': ResearchOutcomeIndicatorContentTypeSerializer,
        'ResearchOutcomeIndicatorDetailSerializer': ResearchOutcomeIndicatorDetailSerializer
    }
