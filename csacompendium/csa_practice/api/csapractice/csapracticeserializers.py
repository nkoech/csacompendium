from csacompendium.csa_practice.models import (
    CsaPractice,
    CsaTheme,
    PracticeLevel,
    PracticeType,
)
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import (
    FieldMethodSerializer,
    get_related_content,
    get_related_content_url,
)
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.csa_practice.api.researchcsapractice.researchcsapracticeserializers import \
    research_csa_practice_serializers

research_csa_practice_serializers = research_csa_practice_serializers()


def csa_practice_serializers():
    """
    CSA practice serializers
    :return: All CSA practice serializers
    :rtype: Object
    """

    class CsaPracticeBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = CsaPractice
            fields = [
                'id',
                'practice_code',
                'csatheme',
                'practicelevel',
                'sub_practice_level',
                'sub_subpractice_level',
                'definition',
                'practicetype',
            ]

    class CsaPracticeRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        csa_theme_url = SerializerMethodField()
        practice_level_url = SerializerMethodField()
        practice_type_url = SerializerMethodField()
        research_relation = SerializerMethodField()

        class Meta:
            model = CsaPractice
            fields = [
                'csa_theme_url',
                'practice_level_url',
                'practice_type_url',
                'research_relation',

            ]

    class CsaPracticeFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_csa_theme_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            if obj.csatheme:
                return get_related_content_url(CsaTheme, obj.csatheme.id)

        def get_practice_level_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            if obj.practicelevel:
                return get_related_content_url(PracticeLevel, obj.practicelevel.id)

        def get_practice_type_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            if obj.practicetype:
                return get_related_content_url(PracticeType, obj.practicetype.id)

        def get_research_relation(self, obj):
            """
            Gets research record
            :param obj: Current record object
            :return: Related research object/record
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchCsaPracticeContentTypeSerializer = research_csa_practice_serializers[
                'ResearchCsaPracticeContentTypeSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchCsaPracticeContentTypeSerializer, obj.research_csa_practice, request
            )
            return related_content

    class CsaPracticeListSerializer(
        CsaPracticeBaseSerializer,
        CsaPracticeRelationBaseSerializer,
        CsaPracticeFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('csa_practice_api:csa_practice_detail', 'slug')

        class Meta:
            model = CsaPractice
            fields = CsaPracticeBaseSerializer.Meta.fields + ['url', ] + \
                     CsaPracticeRelationBaseSerializer.Meta.fields

    class CsaPracticeDetailSerializer(
        CsaPracticeBaseSerializer, CsaPracticeRelationBaseSerializer,
        FieldMethodSerializer, CsaPracticeFieldMethodSerializer
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
            ] + CsaPracticeRelationBaseSerializer.Meta.fields
            model = CsaPractice
            fields = CsaPracticeBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'CsaPracticeListSerializer': CsaPracticeListSerializer,
        'CsaPracticeDetailSerializer': CsaPracticeDetailSerializer
    }
