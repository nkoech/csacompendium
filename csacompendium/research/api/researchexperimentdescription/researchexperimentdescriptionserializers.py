from csacompendium.research.models import (
    ExperimentDescription,
    ResearchExperimentDescription,
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


def research_experiment_description_serializers():
    """
    Research experiment description serializers
    :return: All research experiment description serializers
    :rtype: Object
    """

    class ResearchExperimentDescriptionBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = ResearchExperimentDescription
            fields = [
                'id',
                'experimentdescription',
            ]

    class ResearchExperimentDescriptionRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        experiment_description_url = SerializerMethodField()
        content_type_url = SerializerMethodField()

        class Meta:
            model = ResearchExperimentDescription
            fields = [
                'content_type_url',
                'experiment_description_url',
            ]

    class ResearchExperimentDescriptionFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research experiment description id
            :rtype: String
            """
            return obj.id

        def get_experiment_description_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            if obj.experimentdescription:
                return get_related_content_url(ExperimentDescription, obj.experimentdescription.id)

    def create_research_experiment_description_serializer(model_type=None, pk=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param pk: Primary key
        :param user: Object owner
        :return: Serializer class
        :rtype: Object
        """

        class ResearchExperimentDescriptionCreateSerializer(
            ResearchExperimentDescriptionBaseSerializer,
            CreateSerializerUtil
        ):
            """
            Create a record
            """
            class Meta:
                model = ResearchExperimentDescription
                fields = ResearchExperimentDescriptionBaseSerializer.Meta.fields + ['last_update', 'time_created', ]

            def __init__(self, *args, **kwargs):
                super(ResearchExperimentDescriptionCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = pk
                self.user = user
                self.slugify = False
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Research experiment description object
                :rtype: Object
                """
                experimentdescription = validated_data.get('experimentdescription')
                experiment_description_relation = ResearchExperimentDescription.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    experimentdescription=experimentdescription,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if experiment_description_relation:
                    return experiment_description_relation
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return ResearchExperimentDescriptionCreateSerializer

    class ResearchExperimentDescriptionListSerializer(
        ResearchExperimentDescriptionBaseSerializer, ResearchExperimentDescriptionRelationBaseSerializer,
        FieldMethodSerializer, ResearchExperimentDescriptionFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        research_experiment_description_url = hyperlinked_identity(
            'research_api:research_experiment_description_detail', 'pk'
        )

        class Meta:
            model = ResearchExperimentDescription
            fields = ResearchExperimentDescriptionBaseSerializer.Meta.fields + \
                     ['research_experiment_description_url', ] + \
                     ResearchExperimentDescriptionRelationBaseSerializer.Meta.fields

    class ResearchExperimentDescriptionSerializer(
        ModelSerializer,
        ResearchExperimentDescriptionFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        experiment_description_url = SerializerMethodField()
        relation_id = SerializerMethodField()
        research_experiment_description_url = hyperlinked_identity(
            'research_api:research_experiment_description_detail', 'pk'
        )

        class Meta:
            model = ResearchExperimentDescription
            fields = [
                'relation_id',
                'experimentdescription_id',
                'experiment_description_url',
                'research_experiment_description_url',
            ]

    class ResearchExperimentDescriptionContentTypeSerializer(
        ModelSerializer,
        FieldMethodSerializer,
        ResearchExperimentDescriptionFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        relation_id = SerializerMethodField()
        content_type_url = SerializerMethodField()
        research_experiment_description_url = hyperlinked_identity(
            'research_api:research_experiment_description_detail', 'pk'
        )

        class Meta:
            model = ResearchExperimentDescription
            fields = [
                'relation_id',
                'object_id',
                'content_type_url',
                'research_experiment_description_url',
            ]

    class ResearchExperimentDescriptionDetailSerializer(
        ResearchExperimentDescriptionBaseSerializer, ResearchExperimentDescriptionRelationBaseSerializer,
        FieldMethodSerializer, ResearchExperimentDescriptionFieldMethodSerializer
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
            ] + ResearchExperimentDescriptionRelationBaseSerializer.Meta.fields
            model = ResearchExperimentDescription
            fields = ResearchExperimentDescriptionBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'create_research_experiment_description_serializer': create_research_experiment_description_serializer,
        'ResearchExperimentDescriptionListSerializer': ResearchExperimentDescriptionListSerializer,
        'ResearchExperimentDescriptionSerializer': ResearchExperimentDescriptionSerializer,
        'ResearchExperimentDescriptionContentTypeSerializer': ResearchExperimentDescriptionContentTypeSerializer,
        'ResearchExperimentDescriptionDetailSerializer': ResearchExperimentDescriptionDetailSerializer
    }
