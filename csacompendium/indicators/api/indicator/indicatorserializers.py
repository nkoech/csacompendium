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

outcome_indicator_serializers = outcome_indicator_serializers()

def indicator_serializers():
    """
    Indicator serializers
    :return: All indicator serializers
    :rtype: Object
    """

    class IndicatorBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = Indicator
            fields = [
                'id',
                'subpillar',
                'indicator',
            ]

    class IndicatorRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        subpillar_url = SerializerMethodField()
        outcome_indicators = SerializerMethodField()

        class Meta:
            model = Indicator
            fields = [
                'subpillar_url',
                'outcome_indicators',
            ]

    class IndicatorFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
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
            OutcomeIndicatorListSerializer = outcome_indicator_serializers['OutcomeIndicatorListSerializer']
            related_content = get_related_content(
                obj, OutcomeIndicatorListSerializer, obj.outcome_indicator_relation, request
            )
            return related_content

    class IndicatorListSerializer(
        IndicatorBaseSerializer,
        IndicatorRelationBaseSerializer,
        IndicatorFieldMethodSerializer,
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('indicator_outcome_api:indicator_detail', 'slug')

        class Meta:
            model = Indicator
            fields = IndicatorBaseSerializer.Meta.fields + ['url', ] + \
                     IndicatorRelationBaseSerializer.Meta.fields

    class IndicatorDetailSerializer(
        IndicatorBaseSerializer, IndicatorRelationBaseSerializer,
        FieldMethodSerializer, IndicatorFieldMethodSerializer
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
            ] + IndicatorRelationBaseSerializer.Meta.fields
            model = Indicator
            fields = IndicatorBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'IndicatorListSerializer': IndicatorListSerializer,
        'IndicatorDetailSerializer': IndicatorDetailSerializer
    }
