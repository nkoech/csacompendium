from csacompendium.research_type.models import (
    Author,
    ResearchAuthor,
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


def research_author_serializers():
    """
    Research author serializers
    :return: All research author serializers
    :rtype: Object
    """

    def create_research_author_serializer(model_type=None, pk=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param pk: Primary key
        :param user: Object owner
        :return: Serializer class
        :rtype: Object
        """

        class ResearchAuthorCreateSerializer(ModelSerializer, CreateSerializerUtil):
            """
            Create a record
            """
            class Meta:
                model = ResearchAuthor
                fields = [
                    'id',
                    'author',
                    'last_update',
                    'time_created',
                ]

            def __init__(self, *args, **kwargs):
                super(ResearchAuthorCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = pk
                self.user = user
                self.slugify = False
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Research author object
                :rtype: Object
                """
                author = validated_data.get('author')
                author_relation = ResearchAuthor.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    location=author,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if author_relation:
                    return author_relation
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return ResearchAuthorCreateSerializer

    class ResearchAuthorListSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        author_url = SerializerMethodField()
        content_type_url = SerializerMethodField()
        research_author_url = hyperlinked_identity('research_type_api:research_author_detail', 'pk')

        class Meta:
            model = ResearchAuthor
            fields = [
                'id',
                'author',
                'author_url',
                'content_type_url',
                'research_author_url',
            ]

        def get_author_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(Author, obj.author.id)

    class ResearchAuthorSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        author_url = SerializerMethodField()
        relation_id = SerializerMethodField()
        research_author_url = hyperlinked_identity('research_type_api:research_author_detail', 'pk')

        class Meta:
            model = ResearchAuthor
            fields = [
                'relation_id',
                'author_id',
                'author_url',
                'research_author_url',
            ]

        def get_author_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(Author, obj.author.id)

        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research author id
            :rtype: Integer
            """
            return obj.id

    class ResearchAuthorContentTypeSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        relation_id = SerializerMethodField()
        content_type_url = SerializerMethodField()
        research_author_url = hyperlinked_identity('research_type_api:research_author_detail', 'pk')

        class Meta:
            model = ResearchAuthor
            fields = [
                'relation_id',
                'object_id',
                'content_type_url',
                'research_author_url',
            ]

        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research species id
            :rtype: String
            """
            return obj.id

    class ResearchAuthorDetailSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        author_url = SerializerMethodField()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        content_type_url = SerializerMethodField()

        class Meta:
            model = ResearchAuthor
            fields = [
                'id',
                'author',
                'author_url',
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
                'author_url',
                'content_type_url',
            ]

        def get_author_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(Author, obj.author.id)

    return {
        'create_research_author_serializer': create_research_author_serializer,
        'ResearchAuthorListSerializer': ResearchAuthorListSerializer,
        'ResearchAuthorSerializer': ResearchAuthorSerializer,
        'ResearchAuthorContentTypeSerializer': ResearchAuthorContentTypeSerializer,
        'ResearchAuthorDetailSerializer': ResearchAuthorDetailSerializer
    }
