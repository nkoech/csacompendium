from csacompendium.csa_practice.models import (
    CsaPractice,
    ResearchCsaPractice
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


def research_csa_practice_serializers():
    """
    Research CSA practice serializers
    :return: All research CSA practice serializers
    :rtype: Object
    """

    def create_research_csa_practice_serializer(model_type=None, pk=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param pk: Primary key
        :param user: Object owner
        :return: Serializer class
        :rtype: Object
        """

        class ResearchCsaPracticeCreateSerializer(ModelSerializer, CreateSerializerUtil):
            """
            Create a record
            """
            class Meta:
                model = ResearchCsaPractice
                fields = [
                    'id',
                    'csapractice',
                    'last_update',
                    'time_created',
                ]

            def __init__(self, *args, **kwargs):
                super(ResearchCsaPracticeCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = pk
                self.user = user
                self.slugify = False
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Research CSA practice object
                :rtype: Object
                """
                csapractice = validated_data.get('csapractice')
                csapractice_relation = ResearchCsaPractice.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    csapractice=csapractice,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if csapractice_relation:
                    return csapractice_relation
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return ResearchCsaPracticeCreateSerializer

    class ResearchCsaPracticeListSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        csa_practice_url = SerializerMethodField()
        content_type_url = SerializerMethodField()
        research_csa_practice_url = hyperlinked_identity(
            'csa_practice_api:research_csa_practice_detail', 'pk'
        )

        class Meta:
            model = ResearchCsaPractice
            fields = [
                'id',
                'csapractice',
                'csa_practice_url',
                'content_type_url',
                'research_csa_practice_url',
            ]

        def get_csa_practice_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(CsaPractice, obj.csapractice.id)

    class ResearchCsaPracticeSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        csa_practice_url = SerializerMethodField()
        relation_id = SerializerMethodField()
        research_csa_practice_url = hyperlinked_identity(
            'csa_practice_api:research_csa_practice_detail', 'pk'
        )

        class Meta:
            model = ResearchCsaPractice
            fields = [
                'relation_id',
                'csapractice_id',
                'csa_practice_url',
                'research_csa_practice_url',
            ]

        def get_csa_practice_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(CsaPractice, obj.csapractice.id)

        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research CSA practice id
            :rtype: Integer
            """
            return obj.id

    class ResearchCsaPracticeContentTypeSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        relation_id = SerializerMethodField()
        content_type_url = SerializerMethodField()
        research_csa_practice_url = hyperlinked_identity(
            'csa_practice_api:research_csa_practice_detail', 'pk'
        )

        class Meta:
            model = ResearchCsaPractice
            fields = [
                'relation_id',
                'object_id',
                'content_type_url',
                'research_csa_practice_url',
            ]

        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research CSA practice id
            :rtype: String
            """
            return obj.id

    class ResearchCsaPracticeDetailSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        csa_practice_url = SerializerMethodField()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        content_type_url = SerializerMethodField()

        class Meta:
            model = ResearchCsaPractice
            fields = [
                'id',
                'csapractice',
                'csa_practice_url',
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
                'csa_practice_url',
                'content_type_url',
            ]

        def get_csa_practice_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(CsaPractice, obj.csapractice.id)

    return {
        'create_research_csa_practice_serializer': create_research_csa_practice_serializer,
        'ResearchCsaPracticeListSerializer': ResearchCsaPracticeListSerializer,
        'ResearchCsaPracticeSerializer': ResearchCsaPracticeSerializer,
        'ResearchCsaPracticeContentTypeSerializer': ResearchCsaPracticeContentTypeSerializer,
        'ResearchCsaPracticeDetailSerializer': ResearchCsaPracticeDetailSerializer
    }
