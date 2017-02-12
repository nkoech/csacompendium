from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research_type.api.researchauthor.researchauthorserializer import research_author_serializers
from csacompendium.research_type.models import Author
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content


def author_serializers():
    """
    Author serializers
    :return: All author serializers
    :rtype: Object
    """

    class AuthorBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = Author
            fields = [
                'author_code',
                'first_name',
                'middle_name',
                'last_name',
            ]

    class AuthorListSerializer(AuthorBaseSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_type_api:author_detail', 'slug')

        class Meta:
            model = Author
            fields = AuthorBaseSerializer.Meta.fields + ['url', ]

    class AuthorDetailSerializer(AuthorBaseSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        research_author_serializers = research_author_serializers()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        research = SerializerMethodField()

        class Meta:
            common_fields = [
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'research',
            ]
            model = Author
            fields = ['id', ] + AuthorBaseSerializer.Meta.fields + ['author_bio', ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_research(self, obj):
            """
            :param obj: Current record object
            :return: Locations in a country
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchAuthorSerializer = self.research_author_serializers['ResearchAuthorSerializer']
            related_content = get_related_content(obj, ResearchAuthorSerializer, obj.research_author, request)
            return related_content

    return {
        'AuthorListSerializer': AuthorListSerializer,
        'AuthorDetailSerializer': AuthorDetailSerializer
    }
