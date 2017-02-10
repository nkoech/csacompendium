from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.indicators.api.outcomeindicator.outcomeindicatorserializers import outcome_indicator_serializers
from csacompendium.indicators.models import IndicatorType
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content


def indicator_type_serializers():
    """
    Indicator type serializers
    :return: All indicator type serializers
    :rtype: Object
    """

    class IndicatorTypeListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('indicator_outcome_api:indicator_type_detail', 'slug')

        class Meta:
            model = IndicatorType
            fields = [
                'indicator_type',
                'url',
            ]

    class IndicatorTypeDetailSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        outcome_indicator_serializers = outcome_indicator_serializers()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        outcome_indicators = SerializerMethodField()

        class Meta:
            common_fields = [
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'outcome_indicators',
            ]
            model = IndicatorType
            fields = [
                'id',
                'indicator_type',
            ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_outcome_indicators(self, obj):
            """
            :param obj: Current record object
            :return: Outcome indicatoir related to indicator category
            :rtype: Object/record
            """
            request = self.context['request']
            OutcomeIndicatorListSerializer = self.outcome_indicator_serializers['OutcomeIndicatorListSerializer']
            related_content = get_related_content(
                obj, OutcomeIndicatorListSerializer, obj.outcome_indicator_relation, request
            )
            return related_content

    return {
        'IndicatorTypeListSerializer': IndicatorTypeListSerializer,
        'IndicatorTypeDetailSerializer': IndicatorTypeDetailSerializer
    }
