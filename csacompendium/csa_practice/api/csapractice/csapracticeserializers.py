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
                'sub_practice_level',
                'definition',
            ]

    class CsaPracticeListSerializer(CsaPracticeBaseSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('csa_practice_api:csa_practice_detail', 'slug')

        class Meta:
            model = CsaPractice
            fields = ['practice_code', ] + CsaPracticeBaseSerializer.Meta.fields + ['url', ]

    class CsaPracticeDetailSerializer(CsaPracticeBaseSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        csa_theme_url = SerializerMethodField()
        practice_level_url = SerializerMethodField()
        practice_type_url = SerializerMethodField()
        research_csa_practice_serializers = research_csa_practice_serializers()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        research_relation = SerializerMethodField()

        class Meta:
            common_fields = [
                'csa_theme_url',
                'practice_level_url',
                'practice_type_url',
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'research_relation',
            ]
            model = CsaPractice
            fields = [
                'id',
                'practice_code',
                'csatheme',
                'practicelevel', ] + \
                CsaPracticeBaseSerializer.Meta.fields + \
                ['practicetype', ] + \
                common_fields
            read_only_fields = ['id', ] + common_fields

        def get_csa_theme_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(CsaTheme, obj.csatheme.id)

        def get_practice_level_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(PracticeLevel, obj.practicelevel.id)

        def get_practice_type_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(PracticeType, obj.practicetype.id)

        def get_research_relation(self, obj):
            """
            Gets control/treatment research record
            :param obj: Current record object
            :return: Related research object/record
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchCsaPracticeContentTypeSerializer = self.research_csa_practice_serializers[
                'ResearchCsaPracticeContentTypeSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchCsaPracticeContentTypeSerializer, obj.research_csa_practice, request
            )
            return related_content

    return {
        'CsaPracticeListSerializer': CsaPracticeListSerializer,
        'CsaPracticeDetailSerializer': CsaPracticeDetailSerializer
    }
