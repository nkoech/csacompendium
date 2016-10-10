from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
# from csacompendium.research.api.research.researchserializers import research_serializers
from csacompendium.research.models import Author
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity


def author_serializers():
    """
    Author serializers
    :return: All author  serializers
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
        url = hyperlinked_identity('research_api:author_detail', 'slug')

        class Meta:
            model = Author
            fields = AuthorBaseSerializer.Meta.fields + ['url', ]

    class AuthorDetailSerializer(AuthorBaseSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        # research_serializers = research_serializers()
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

        def get_user(self, obj):
            """
            :param obj: Current record object
            :return: Name of user who created the record
            :rtype: String
            """
            return str(obj.user.username)

        def get_modified_by(self, obj):
            """
            :param obj: Current record object
            :return: Name of user who edited a record
            :rtype: String
            """
            return str(obj.modified_by.username)

        def get_research(self, obj):
            """
            :param obj: Current record object
            :return: Research object
            :rtype: Object/record
            """
            request = self.context['request']
            # ResearchListSerializer = self.research_serializers['ResearchListSerializer']
            try:
                pass
                # research = ResearchListSerializer(
                #     obj.research_relation,
                #     context={'request': request},
                #     many=True
                # ).data
                # return research
            except obj.DoesNotExist:
                return None

    return {
        'AuthorListSerializer': AuthorListSerializer,
        'AuthorDetailSerializer': AuthorDetailSerializer
    }
