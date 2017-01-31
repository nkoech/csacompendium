from csacompendium.research_type.api.serializers import control_research_serializers
from csacompendium.research_type.api.serializers import treatment_research_serializers
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
    SerializerMethodField,
)


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

    class CsaPracticeCreateSerializer(CsaPracticeBaseSerializer):
        """
        Create a record
        """
        user = SerializerMethodField()
        modified_by = SerializerMethodField()

        class Meta:
            common_fields = [
                'user',
                'modified_by',
                'last_update',
                'time_created',
            ]
            model = CsaPractice
            fields = ['id', 'practice_code', 'csatheme', 'practicelevel', ] + \
                     CsaPracticeBaseSerializer.Meta.fields + ['practicetype', ] + common_fields
            read_only_fields = ['id', ] + common_fields

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
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        control_research = SerializerMethodField()
        treatment_research = SerializerMethodField()

        class Meta:
            common_fields = [
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'control_research',
                'treatment_research',
            ]
            model = CsaPractice
            fields = ['id', 'practice_code', 'csa_theme_url', 'practice_level_url', ] + \
                     CsaPracticeBaseSerializer.Meta.fields + ['practice_type_url', ] + common_fields
            read_only_fields = ['id', 'csa_theme_url', 'practice_level_url', 'practice_type_url', ] + common_fields

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

        def get_control_research(self, obj):
            """
            Get related control research data
            :param obj: Current record object
            :return: Control research of a given CSA practice
            :rtype: Object/record
            """
            request = self.context['request']
            ControlResearchListSerializer = control_research_serializers['ControlResearchListSerializer']
            related_content = get_related_content(obj, ControlResearchListSerializer, obj.control_research, request)
            return related_content

        def get_treatment_research(self, obj):
            """
            Get related treatment research data
            :param obj: Current record object
            :return: Treatment research of a given CSA practice
            :rtype: Object/record
            """
            request = self.context['request']
            TreatmentResearchListSerializer = treatment_research_serializers['TreatmentResearchListSerializer']
            related_content = get_related_content(
                obj, TreatmentResearchListSerializer, obj.treatment_research, request
            )
            return related_content

    return {
        'CsaPracticeCreateSerializer': CsaPracticeCreateSerializer,
        'CsaPracticeListSerializer': CsaPracticeListSerializer,
        'CsaPracticeDetailSerializer': CsaPracticeDetailSerializer
    }
