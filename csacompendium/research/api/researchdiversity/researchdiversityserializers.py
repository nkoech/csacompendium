from csacompendium.research.models import (
    Diversity,
    ResearchDiversity,
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


def research_diversity_serializers():
    """
    Research diversity serializers
    :return: All research diversity serializers
    :rtype: Object
    """

    class ResearchDiversityBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = ResearchDiversity
            fields = [
                'id',
                'diversity',
            ]

    class ResearchDiversityRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        diversity_url = SerializerMethodField()
        content_type_url = SerializerMethodField()

        class Meta:
            model = ResearchDiversity
            fields = [
                'content_type_url',
                'diversity_url',
            ]

    class ResearchDiversityFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research diversity id
            :rtype: String
            """
            return obj.id

        def get_diversity_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            if obj.diversity:
                return get_related_content_url(Diversity, obj.diversity.id)

    def create_research_diversity_serializer(model_type=None, pk=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param pk: Primary key
        :param user: Object owner
        :return: Serializer class
        :rtype: Object
        """

        class ResearchDiversityCreateSerializer(
            ResearchDiversityBaseSerializer,
            CreateSerializerUtil
        ):
            """
            Create a record
            """
            class Meta:
                model = ResearchDiversity
                fields = ResearchDiversityBaseSerializer.Meta.fields + ['last_update', 'time_created', ]

            def __init__(self, *args, **kwargs):
                super(ResearchDiversityCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = pk
                self.user = user
                self.slugify = False
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Research diversity object
                :rtype: Object
                """
                diversity = validated_data.get('diversity')
                diversity_relation = ResearchDiversity.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    diversity=diversity,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if diversity_relation:
                    return diversity_relation
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return ResearchDiversityCreateSerializer

    class ResearchDiversityListSerializer(
        ResearchDiversityBaseSerializer, ResearchDiversityRelationBaseSerializer,
        FieldMethodSerializer, ResearchDiversityFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        research_diversity_url = hyperlinked_identity(
            'research_api:research_diversity_detail', 'pk'
        )

        class Meta:
            model = ResearchDiversity
            fields = ResearchDiversityBaseSerializer.Meta.fields + \
                     ['research_diversity_url', ] + \
                     ResearchDiversityRelationBaseSerializer.Meta.fields

    class ResearchDiversitySerializer(
        ModelSerializer,
        ResearchDiversityFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        diversity_url = SerializerMethodField()
        relation_id = SerializerMethodField()
        research_diversity_url = hyperlinked_identity(
            'research_api:research_diversity_detail', 'pk'
        )

        class Meta:
            model = ResearchDiversity
            fields = [
                'relation_id',
                'diversity_id',
                'diversity_url',
                'research_diversity_url',
            ]

    class ResearchDiversityContentTypeSerializer(
        ModelSerializer,
        FieldMethodSerializer,
        ResearchDiversityFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        relation_id = SerializerMethodField()
        content_type_url = SerializerMethodField()
        research_diversity_url = hyperlinked_identity(
            'research_api:research_diversity_detail', 'pk'
        )

        class Meta:
            model = ResearchDiversity
            fields = [
                'relation_id',
                'object_id',
                'content_type_url',
                'research_diversity_url',
            ]

    class ResearchDiversityDetailSerializer(
        ResearchDiversityBaseSerializer, ResearchDiversityRelationBaseSerializer,
        FieldMethodSerializer, ResearchDiversityFieldMethodSerializer
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
            ] + ResearchDiversityRelationBaseSerializer.Meta.fields
            model = ResearchDiversity
            fields = ResearchDiversityBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'create_research_diversity_serializer': create_research_diversity_serializer,
        'ResearchDiversityListSerializer': ResearchDiversityListSerializer,
        'ResearchDiversitySerializer': ResearchDiversitySerializer,
        'ResearchDiversityContentTypeSerializer': ResearchDiversityContentTypeSerializer,
        'ResearchDiversityDetailSerializer': ResearchDiversityDetailSerializer
    }
