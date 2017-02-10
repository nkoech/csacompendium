from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.indicators.api.outcomeindicator.outcomeindicatorserializers import outcome_indicator_serializers
from csacompendium.indicators.models import Indicator, Subpillar
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import (
    FieldMethodSerializer,
    get_related_content_url,
    get_related_content,
)


def indicator_serializers():
    """
    Indicator serializers
    :return: All indicator serializers
    :rtype: Object
    """

    class IndicatorListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('indicator_outcome_api:indicator_detail', 'slug')

        class Meta:
            model = Indicator
            fields = [
                'indicator',
                'url',
            ]

    class IndicatorDetailSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        outcome_indicator_serializers = outcome_indicator_serializers()
        subpillar_url = SerializerMethodField()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        outcome_indicators = SerializerMethodField()

        class Meta:
            common_fields = [
                'subpillar_url',
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'outcome_indicators',
            ]
            model = Indicator
            fields = [
                'id',
                'subpillar',
                'indicator',
            ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_subpillar_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(Subpillar, obj.subpillar.id)

        def get_outcome_indicators(self, obj):
            """
            :param obj: Current record object
            :return: Outcome indicator of the indicator record
            :rtype: Object/record
            """
            request = self.context['request']
            OutcomeIndicatorListSerializer = self.outcome_indicator_serializers['OutcomeIndicatorListSerializer']
            related_content = get_related_content(
                obj, OutcomeIndicatorListSerializer, obj.outcome_indicator_relation, request
            )
            return related_content

    return {
        'IndicatorListSerializer': IndicatorListSerializer,
        'IndicatorDetailSerializer': IndicatorDetailSerializer
    }
