from csacompendium.research.models import (
    ExperimentReplicate,
    ResearchExperimentReplicate,
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


def research_experiment_replicate_serializers():
    """
    Research experiment replicate serializers
    :return: All research experiment replicate serializers
    :rtype: Object
    """

    class ResearchExperimentReplicateBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = ResearchExperimentReplicate
            fields = [
                'id',
                'experimentreplicate',
            ]

    class ResearchExperimentReplicateRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        experiment_replicate_url = SerializerMethodField()
        content_type_url = SerializerMethodField()

        class Meta:
            model = ResearchExperimentReplicate
            fields = [
                'content_type_url',
                'experiment_replicate_url',
            ]

    class ResearchExperimentReplicateFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_experiment_replicate_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            if obj.experimentreplicate:
                return get_related_content_url(ExperimentReplicate, obj.experimentreplicate.id)

    def create_research_experiment_replicate_serializer(model_type=None, pk=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param pk: Primary key
        :param user: Object owner
        :return: Serializer class
        :rtype: Object
        """

        class ResearchExperimentReplicateCreateSerializer(
            ResearchExperimentReplicateBaseSerializer,
            CreateSerializerUtil
        ):
            """
            Create a record
            """
            class Meta:
                model = ResearchExperimentReplicate
                fields = ResearchExperimentReplicateBaseSerializer.Meta.fields + ['last_update', 'time_created', ]

            def __init__(self, *args, **kwargs):
                super(ResearchExperimentReplicateCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = pk
                self.user = user
                self.slugify = False
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Research experiment replicate object
                :rtype: Object
                """
                experimentreplicate = validated_data.get('experimentreplicate')
                experiment_replicate_relation = ResearchExperimentReplicate.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    experimentreplicate=experimentreplicate,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if experiment_replicate_relation:
                    return experiment_replicate_relation
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return ResearchExperimentReplicateCreateSerializer

    class ResearchExperimentReplicateListSerializer(
        ResearchExperimentReplicateBaseSerializer, ResearchExperimentReplicateRelationBaseSerializer,
        FieldMethodSerializer, ResearchExperimentReplicateFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        research_experiment_replicate_url = hyperlinked_identity(
            'research_api:research_experiment_replicate_detail', 'pk'
        )

        class Meta:
            model = ResearchExperimentReplicate
            fields = ResearchExperimentReplicateBaseSerializer.Meta.fields + \
                     ['research_experiment_replicate_url', ] + \
                     ResearchExperimentReplicateRelationBaseSerializer.Meta.fields

    class ResearchExperimentReplicateSerializer(ModelSerializer, ResearchExperimentReplicateFieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        experiment_replicate_url = SerializerMethodField()
        relation_id = SerializerMethodField()
        research_experiment_replicate_url = hyperlinked_identity(
            'research_api:research_experiment_replicate_detail', 'pk'
        )

        class Meta:
            model = ResearchExperimentReplicate
            fields = [
                'relation_id',
                'experimentreplicate_id',
                'experiment_replicate_url',
                'research_experiment_replicate_url',
            ]

        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research experiment replicate id
            :rtype: Integer
            """
            return obj.id

    class ResearchExperimentReplicateContentTypeSerializer(
        ModelSerializer,
        FieldMethodSerializer,
        ResearchExperimentReplicateFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        relation_id = SerializerMethodField()
        content_type_url = SerializerMethodField()
        research_experiment_replicate_url = hyperlinked_identity(
            'research_api:research_experiment_replicate_detail', 'pk'
        )

        class Meta:
            model = ResearchExperimentReplicate
            fields = [
                'relation_id',
                'object_id',
                'content_type_url',
                'research_experiment_replicate_url',
            ]

        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research experiment replicate id
            :rtype: String
            """
            return obj.id

    class ResearchExperimentReplicateDetailSerializer(
        ResearchExperimentReplicateBaseSerializer, ResearchExperimentReplicateRelationBaseSerializer,
        FieldMethodSerializer, ResearchExperimentReplicateFieldMethodSerializer
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
            ] + ResearchExperimentReplicateRelationBaseSerializer.Meta.fields
            model = ResearchExperimentReplicate
            fields = ResearchExperimentReplicateBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'create_research_experiment_replicate_serializer': create_research_experiment_replicate_serializer,
        'ResearchExperimentReplicateListSerializer': ResearchExperimentReplicateListSerializer,
        'ResearchExperimentReplicateSerializer': ResearchExperimentReplicateSerializer,
        'ResearchExperimentReplicateContentTypeSerializer': ResearchExperimentReplicateContentTypeSerializer,
        'ResearchExperimentReplicateDetailSerializer': ResearchExperimentReplicateDetailSerializer
    }
