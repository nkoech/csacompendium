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
from csacompendium.indicators.api.researchoutcomeindicator.researchoutcomeindicatorserializers \
    import research_outcome_indicator_serializers

research_outcome_indicator_serializers = research_outcome_indicator_serializers()


def outcome_indicator_serializers():
    """
    Outcome indicator serializers
    :return: All outcome indicator serializers
    :rtype: Object
    """

    class OutcomeIndicatorBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = OutcomeIndicator
            fields = [
                'id',
                'indicator_code',
                'indicator',
                'subindicator',
                'definition',
                'common_uom',
                'indicatortype',
            ]

    class OutcomeIndicatorRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        indicator_url = SerializerMethodField()
        indicator_type_url = SerializerMethodField()
        research_relation = SerializerMethodField()

        class Meta:
            model = OutcomeIndicator
            fields = [
                'indicator_url',
                'indicator_type_url',
                'research_relation',
            ]

    class OutcomeIndicatorFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
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

        def get_research_relation(self, obj):
            """
            Gets research record
            :param obj: Current record object
            :return: Related research object/record
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchOutcomeIndicatorContentTypeSerializer = research_outcome_indicator_serializers[
                'ResearchOutcomeIndicatorContentTypeSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchOutcomeIndicatorContentTypeSerializer, obj.research_outcome_indicator, request
            )
            return related_content

    class OutcomeIndicatorListSerializer(
        OutcomeIndicatorBaseSerializer,
        OutcomeIndicatorRelationBaseSerializer,
        OutcomeIndicatorFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('indicator_outcome_api:outcome_indicator_detail', 'slug')

        class Meta:
            model = OutcomeIndicator
            fields = OutcomeIndicatorBaseSerializer.Meta.fields + ['url', ] + \
                     OutcomeIndicatorRelationBaseSerializer.Meta.fields

    class OutcomeIndicatorDetailSerializer(
        OutcomeIndicatorBaseSerializer, OutcomeIndicatorRelationBaseSerializer,
        FieldMethodSerializer, OutcomeIndicatorFieldMethodSerializer
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
            ] + OutcomeIndicatorRelationBaseSerializer.Meta.fields
            model = OutcomeIndicator
            fields = OutcomeIndicatorBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'OutcomeIndicatorListSerializer': OutcomeIndicatorListSerializer,
        'OutcomeIndicatorDetailSerializer': OutcomeIndicatorDetailSerializer
    }
