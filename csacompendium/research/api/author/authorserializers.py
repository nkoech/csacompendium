from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.researchauthor.researchauthorserializer import research_author_serializers
from csacompendium.research.models import Author
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

research_author_serializers = research_author_serializers()


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
                'id',
                'author_code',
                'first_name',
                'middle_name',
                'last_name',
                'author_bio',
            ]

    class AuthorRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        research_relation = SerializerMethodField()

        class Meta:
            model = Author
            fields = [
                'research_relation',
            ]

    class AuthorFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_research_relation(self, obj):
            """
            Gets research record
            :param obj: Current record object
            :return: Related research object/record
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchAuthorContentTypeSerializer = research_author_serializers[
                'ResearchAuthorContentTypeSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchAuthorContentTypeSerializer, obj.research_author_relation, request
            )
            return related_content

    class AuthorListSerializer(
        AuthorBaseSerializer, AuthorRelationBaseSerializer, AuthorFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:author_detail', 'slug')

        class Meta:
            model = Author
            fields = AuthorBaseSerializer.Meta.fields + ['url', ] + AuthorRelationBaseSerializer.Meta.fields

    class AuthorDetailSerializer(
        AuthorBaseSerializer, AuthorRelationBaseSerializer, FieldMethodSerializer, AuthorFieldMethodSerializer
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
            ] + AuthorRelationBaseSerializer.Meta.fields
            model = Author
            fields = AuthorBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'AuthorListSerializer': AuthorListSerializer,
        'AuthorDetailSerializer': AuthorDetailSerializer
    }
