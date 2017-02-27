from csacompendium.research.models import (
    ExperimentUnit,
    ResearchExperimentUnit,
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


def research_experiment_unit_serializers():
    """
    Research experiment unit serializers
    :return: All research experiment unit serializers
    :rtype: Object
    """

    def create_research_experiment_unit_serializer(model_type=None, pk=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param pk: Primary key
        :param user: Object owner
        :return: Serializer class
        :rtype: Object
        """

        class ResearchExperimentUnitCreateSerializer(ModelSerializer, CreateSerializerUtil):
            """
            Create a record
            """
            class Meta:
                model = ResearchExperimentUnit
                fields = [
                    'id',
                    'experimentunit',
                    'upper_soil_depth',
                    'lower_soil_depth',
                    'incubation_days',
                    'last_update',
                    'time_created',
                ]

            def __init__(self, *args, **kwargs):
                super(ResearchExperimentUnitCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = pk
                self.user = user
                self.slugify = False
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Research experiment unit object
                :rtype: Object
                """
                experimentunit = validated_data.get('experimentunit')
                upper_soil_depth = validated_data.get('upper_soil_depth')
                lower_soil_depth = validated_data.get('lower_soil_depth')
                incubation_days = validated_data.get('incubation_days')
                experimentunit_relation = ResearchExperimentUnit.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    experimentunit=experimentunit,
                    upper_soil_depth=upper_soil_depth,
                    lower_soil_depth=lower_soil_depth,
                    incubation_days=incubation_days,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if experimentunit_relation:
                    return experimentunit_relation
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return ResearchExperimentUnitCreateSerializer

    class ResearchExperimentUnitListSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        experiment_unit_url = SerializerMethodField()
        content_type_url = SerializerMethodField()
        research_experiment_unit_url = hyperlinked_identity(
            'research_api:research_experiment_unit_detail', 'pk'
        )

        class Meta:
            model = ResearchExperimentUnit
            fields = [
                'id',
                'experimentunit',
                'experiment_unit_url',
                'content_type_url',
                'research_experiment_unit_url',
            ]

        def get_experiment_unit_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(ExperimentUnit, obj.experimentunit.id)

    class ResearchExperimentUnitSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        experiment_unit_url = SerializerMethodField()
        relation_id = SerializerMethodField()
        research_experiment_unit_url = hyperlinked_identity(
            'research_api:research_experiment_unit_detail', 'pk'
        )

        class Meta:
            model = ResearchExperimentUnit
            fields = [
                'relation_id',
                'experimentunit_id',
                'experiment_unit_url',
                'research_experiment_unit_url',
            ]

        def get_experiment_unit_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(ResearchExperimentUnit, obj.experimentunit.id)

        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research experiment unit id
            :rtype: Integer
            """
            return obj.id

    class ResearchExperimentUnitContentTypeSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        relation_id = SerializerMethodField()
        content_type_url = SerializerMethodField()
        research_experiment_unit_url = hyperlinked_identity(
            'research_api:research_experiment_unit_detail', 'pk'
        )

        class Meta:
            model = ResearchExperimentUnit
            fields = [
                'relation_id',
                'object_id',
                'content_type_url',
                'research_experiment_unit_url',
            ]

        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research experiment unit id
            :rtype: String
            """
            return obj.id

    class ResearchExperimentUnitDetailSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        experiment_unit_url = SerializerMethodField()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        content_type_url = SerializerMethodField()

        class Meta:
            model = ResearchExperimentUnit
            fields = [
                'id',
                'experimentunit',
                'experiment_unit_url',
                'upper_soil_depth',
                'lower_soil_depth',
                'incubation_days',
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'content_type_url',
            ]
            read_only_fields = [
                'id',
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'experiment_unit_url',
                'content_type_url',
            ]

        def get_experiment_unit_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(ExperimentUnit, obj.experimentunit.id)

    return {
        'create_research_experiment_unit_serializer': create_research_experiment_unit_serializer,
        'ResearchExperimentUnitListSerializer': ResearchExperimentUnitListSerializer,
        'ResearchExperimentUnitSerializer': ResearchExperimentUnitSerializer,
        'ResearchExperimentUnitContentTypeSerializer': ResearchExperimentUnitContentTypeSerializer,
        'ResearchExperimentUnitDetailSerializer': ResearchExperimentUnitDetailSerializer
    }