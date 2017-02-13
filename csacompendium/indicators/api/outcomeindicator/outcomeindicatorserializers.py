from csacompendium.indicators.models import (
    OutcomeIndicator,
    IndicatorType,
    Indicator,
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
# from csacompendium.research.api.researchoutcomeindicator.researchoutcomeindicatorserializers \
#     import research_outcome_indicator_serializers


def outcome_indicator_serializers():
    """
    Outcome indicator serializers
    :return: All outcome indicator serializers
    :rtype: Object
    """

    class OutcomeIndicatorListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('indicator_outcome_api:outcome_indicator_detail', 'slug')

        class Meta:
            model = OutcomeIndicator
            fields = [
                'id',
                'indicator_code',
                'subindicator',
                'definition',
                'common_uom',
                'url',
            ]

    class OutcomeIndicatorDetailSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        indicator_url = SerializerMethodField()
        indicator_type_url = SerializerMethodField()
        # research_outcome_indicator_serializers = research_outcome_indicator_serializers()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        research = SerializerMethodField()

        class Meta:
            common_fields = [
                'indicator_url',
                'indicator_type_url',
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'research',
            ]
            model = OutcomeIndicator
            fields = [
                'id',
                'indicator_code',
                'indicator',
                'subindicator',
                'definition',
                'common_uom',
                'indicatortype',
            ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_indicator_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(Indicator, obj.indicator.id)

        def get_indicator_type_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(IndicatorType, obj.indicatortype.id)

        # def get_research(self, obj):
        #     """
        #     :param obj: Current record object
        #     :return: Research in a location
        #     :rtype: Object/record
        #     """
        #     request = self.context['request']
        #     ResearchOutcomeSerializer = self.research_outcome_indicator_serializers['ResearchOutcomeSerializer']
        #     related_content = get_related_content(
        #         obj, ResearchOutcomeSerializer, obj.research_outcome_indicator, request
        #     )
        #     return related_content

    return {
        'OutcomeIndicatorListSerializer': OutcomeIndicatorListSerializer,
        'OutcomeIndicatorDetailSerializer': OutcomeIndicatorDetailSerializer
    }
