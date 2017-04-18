from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.researchauthor.researchauthorserializer import research_author_serializers
from csacompendium.research.models import Journal
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

research_author_serializers = research_author_serializers()


def journal_serializers():
    """
    Journal serializers
    :return: All journal serializers
    :rtype: Object
    """

    class JournalBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = Journal
            fields = [
                'id',
                'journal_tag',
                'publication_year',
            ]

    class JournalRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        research_author = SerializerMethodField()

        class Meta:
            model = Journal
            fields = [
                'research_author',
            ]

    class JournalFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_research_author(self, obj):
            """
            :param obj: Current record object
            :return: Research author object
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchAuthorListSerializer = research_author_serializers['ResearchAuthorListSerializer']
            related_content = get_related_content(
                obj, ResearchAuthorListSerializer, obj.research_author_relation, request
            )
            return related_content

    class JournalListSerializer(
        JournalBaseSerializer,
        JournalRelationBaseSerializer,
        JournalFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:journal_detail', 'slug')

        class Meta:
            model = Journal
            fields = JournalBaseSerializer.Meta.fields + ['url', ] + \
                     JournalRelationBaseSerializer.Meta.fields

    class JournalDetailSerializer(
        JournalBaseSerializer, JournalRelationBaseSerializer,
        FieldMethodSerializer, JournalFieldMethodSerializer
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
            ] + JournalRelationBaseSerializer.Meta.fields
            model = Journal
            fields = JournalBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'JournalListSerializer': JournalListSerializer,
        'JournalDetailSerializer': JournalDetailSerializer
    }
