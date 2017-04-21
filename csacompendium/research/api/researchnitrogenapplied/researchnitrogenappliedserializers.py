from csacompendium.research.models import (
    NitrogenApplied,
    ResearchNitrogenApplied,
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


def research_nitrogen_applied_serializers():
    """
    Research nitrogen applied serializers
    :return: All research nitrogen applied serializers
    :rtype: Object
    """

    class ResearchNitrogenAppliedBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = ResearchNitrogenApplied
            fields = [
                'id',
                'nitrogenapplied',
            ]

    class ResearchNitrogenAppliedRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        nitrogen_applied_url = SerializerMethodField()
        content_type_url = SerializerMethodField()

        class Meta:
            model = ResearchNitrogenApplied
            fields = [
                'content_type_url',
                'nitrogen_applied_url',
            ]

    class ResearchNitrogenAppliedFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research nitrogen applied id
            :rtype: String
            """
            return obj.id

        def get_nitrogen_applied_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            if obj.nitrogenapplied:
                return get_related_content_url(NitrogenApplied, obj.nitrogenapplied.id)

    def create_research_nitrogen_applied_serializer(model_type=None, pk=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param pk: Primary key
        :param user: Object owner
        :return: Serializer class
        :rtype: Object
        """

        class ResearchNitrogenAppliedCreateSerializer(
            ResearchNitrogenAppliedBaseSerializer,
            CreateSerializerUtil
        ):
            """
            Create a record
            """
            class Meta:
                model = ResearchNitrogenApplied
                fields = ResearchNitrogenAppliedBaseSerializer.Meta.fields + ['last_update', 'time_created', ]

            def __init__(self, *args, **kwargs):
                super(ResearchNitrogenAppliedCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = pk
                self.user = user
                self.slugify = False
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Research nitrogen applied object
                :rtype: Object
                """
                nitrogenapplied = validated_data.get('nitrogenapplied')
                nitrogen_applied_relation = ResearchNitrogenApplied.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    nitrogenapplied=nitrogenapplied,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if nitrogen_applied_relation:
                    return nitrogen_applied_relation
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return ResearchNitrogenAppliedCreateSerializer

    class ResearchNitrogenAppliedListSerializer(
        ResearchNitrogenAppliedBaseSerializer, ResearchNitrogenAppliedRelationBaseSerializer,
        FieldMethodSerializer, ResearchNitrogenAppliedFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        research_nitrogen_applied_url = hyperlinked_identity(
            'research_api:research_nitrogen_applied_detail', 'pk'
        )

        class Meta:
            model = ResearchNitrogenApplied
            fields = ResearchNitrogenAppliedBaseSerializer.Meta.fields + \
                     ['research_nitrogen_applied_url', ] + \
                     ResearchNitrogenAppliedRelationBaseSerializer.Meta.fields

    class ResearchNitrogenAppliedSerializer(ModelSerializer, ResearchNitrogenAppliedFieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        nitrogen_applied_url = SerializerMethodField()
        relation_id = SerializerMethodField()
        research_nitrogen_applied_url = hyperlinked_identity(
            'research_api:research_nitrogen_applied_detail', 'pk'
        )

        class Meta:
            model = ResearchNitrogenApplied
            fields = [
                'relation_id',
                'nitrogenapplied_id',
                'nitrogen_applied_url',
                'research_nitrogen_applied_url',
            ]

    class ResearchNitrogenAppliedContentTypeSerializer(
        ModelSerializer,
        FieldMethodSerializer,
        ResearchNitrogenAppliedFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        relation_id = SerializerMethodField()
        content_type_url = SerializerMethodField()
        research_nitrogen_applied_url = hyperlinked_identity(
            'research_api:research_nitrogen_applied_detail', 'pk'
        )

        class Meta:
            model = ResearchNitrogenApplied
            fields = [
                'relation_id',
                'object_id',
                'content_type_url',
                'research_nitrogen_applied_url',
            ]

    class ResearchNitrogenAppliedDetailSerializer(
        ResearchNitrogenAppliedBaseSerializer, ResearchNitrogenAppliedRelationBaseSerializer,
        FieldMethodSerializer, ResearchNitrogenAppliedFieldMethodSerializer
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
            ] + ResearchNitrogenAppliedRelationBaseSerializer.Meta.fields
            model = ResearchNitrogenApplied
            fields = ResearchNitrogenAppliedBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'create_research_nitrogen_applied_serializer': create_research_nitrogen_applied_serializer,
        'ResearchNitrogenAppliedListSerializer': ResearchNitrogenAppliedListSerializer,
        'ResearchNitrogenAppliedSerializer': ResearchNitrogenAppliedSerializer,
        'ResearchNitrogenAppliedContentTypeSerializer': ResearchNitrogenAppliedContentTypeSerializer,
        'ResearchNitrogenAppliedDetailSerializer': ResearchNitrogenAppliedDetailSerializer
    }
