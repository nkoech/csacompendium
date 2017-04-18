from csacompendium.research.models import (
    Author,
    Journal,
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

    class ResearchAuthorBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = ResearchAuthor
            fields = [
                'id',
                'author',
                'journal',
            ]

    class ResearchAuthorRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        author_url = SerializerMethodField()
        journal_url = SerializerMethodField()
        content_type_url = SerializerMethodField()

        class Meta:
            model = ResearchAuthor
            fields = [
                'content_type_url',
                'author_url',
                'journal_url',
            ]

    class ResearchAuthorFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_author_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            if obj.author:
                return get_related_content_url(Author, obj.author.id)

        def get_journal_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            if obj.journal:
                return get_related_content_url(Journal, obj.journal.id)

    def create_research_author_serializer(model_type=None, pk=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param pk: Primary key
        :param user: Object owner
        :return: Serializer class
        :rtype: Object
        """

        class ResearchAuthorCreateSerializer(ResearchAuthorBaseSerializer, CreateSerializerUtil):
            """
            Create a record
            """
            class Meta:
                model = ResearchAuthor
                fields = ResearchAuthorBaseSerializer.Meta.fields + ['last_update', 'time_created', ]

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
                journal = validated_data.get('journal')
                author_relation = ResearchAuthor.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    author=author,
                    journal=journal,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if author_relation:
                    return author_relation
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return ResearchAuthorCreateSerializer

    class ResearchAuthorListSerializer(
        ResearchAuthorBaseSerializer, ResearchAuthorRelationBaseSerializer,
        FieldMethodSerializer, ResearchAuthorFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        research_author_url = hyperlinked_identity('research_api:research_author_detail', 'pk')

        class Meta:
            model = ResearchAuthor
            fields = ResearchAuthorBaseSerializer.Meta.fields + ['research_author_url', ] + \
                     ResearchAuthorRelationBaseSerializer.Meta.fields

    class ResearchAuthorSerializer(ModelSerializer, ResearchAuthorFieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        author_url = SerializerMethodField()
        relation_id = SerializerMethodField()
        research_author_url = hyperlinked_identity('research_api:research_author_detail', 'pk')
        journal_url = SerializerMethodField()

        class Meta:
            model = ResearchAuthor
            fields = [
                'relation_id',
                'author_id',
                'author_url',
                'research_author_url',
                'journal_url',
            ]

        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research author id
            :rtype: Integer
            """
            return obj.id

    class ResearchAuthorContentTypeSerializer(
        ModelSerializer,
        FieldMethodSerializer,
        ResearchAuthorFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        relation_id = SerializerMethodField()
        content_type_url = SerializerMethodField()
        research_author_url = hyperlinked_identity('research_api:research_author_detail', 'pk')
        journal_url = SerializerMethodField()

        class Meta:
            model = ResearchAuthor
            fields = [
                'relation_id',
                'object_id',
                'content_type_url',
                'research_author_url',
                'journal_url',
            ]

        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research author id
            :rtype: String
            """
            return obj.id

    class ResearchAuthorDetailSerializer(
        ResearchAuthorBaseSerializer, ResearchAuthorRelationBaseSerializer,
        FieldMethodSerializer, ResearchAuthorFieldMethodSerializer
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
            ] + ResearchAuthorRelationBaseSerializer.Meta.fields
            model = ResearchAuthor
            fields = ResearchAuthorBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'create_research_author_serializer': create_research_author_serializer,
        'ResearchAuthorListSerializer': ResearchAuthorListSerializer,
        'ResearchAuthorSerializer': ResearchAuthorSerializer,
        'ResearchAuthorContentTypeSerializer': ResearchAuthorContentTypeSerializer,
        'ResearchAuthorDetailSerializer': ResearchAuthorDetailSerializer
    }
