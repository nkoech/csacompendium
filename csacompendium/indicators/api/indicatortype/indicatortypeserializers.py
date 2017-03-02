from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.indicators.api.outcomeindicator.outcomeindicatorserializers import outcome_indicator_serializers
from csacompendium.indicators.models import IndicatorType
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

outcome_indicator_serializers = outcome_indicator_serializers()


def indicator_type_serializers():
    """
    Indicator type serializers
    :return: All indicator type serializers
    :rtype: Object
    """
    class IndicatorTypeBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """

        class Meta:
            model = IndicatorType
            fields = [
                'id',
                'indicator_type',
            ]

    class IndicatorTypeRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        outcome_indicators = SerializerMethodField()

        class Meta:
            model = IndicatorType
            fields = [
                'outcome_indicators'
            ]

    class IndicatorTypeFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_outcome_indicators(self, obj):
            """
            :param obj: Current record object
            :return: Outcome indicatoir related to indicator category
            :rtype: Object/record
            """
            request = self.context['request']
            OutcomeIndicatorListSerializer = outcome_indicator_serializers['OutcomeIndicatorListSerializer']
            related_content = get_related_content(
                obj, OutcomeIndicatorListSerializer, obj.outcome_indicator_relation, request
            )
            return related_content

    class IndicatorTypeListSerializer(
        IndicatorTypeBaseSerializer,
        IndicatorTypeRelationBaseSerializer,
        IndicatorTypeFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('indicator_outcome_api:indicator_type_detail', 'slug')

        class Meta:
            model = IndicatorType
            fields = IndicatorTypeBaseSerializer.Meta.fields + ['url', ] + \
                     IndicatorTypeRelationBaseSerializer.Meta.fields

    class IndicatorTypeDetailSerializer(
        IndicatorTypeBaseSerializer, IndicatorTypeRelationBaseSerializer,
        FieldMethodSerializer, IndicatorTypeFieldMethodSerializer
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
            ] + IndicatorTypeRelationBaseSerializer.Meta.fields
            model = IndicatorType
            fields = IndicatorTypeBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'IndicatorTypeListSerializer': IndicatorTypeListSerializer,
        'IndicatorTypeDetailSerializer': IndicatorTypeDetailSerializer
    }
