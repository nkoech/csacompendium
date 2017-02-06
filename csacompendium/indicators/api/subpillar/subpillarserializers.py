from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.indicators.api.indicator.indicatorserializers import indicator_serializers
from csacompendium.indicators.models import Subpillar
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content


def subpillar_serializers():
    """
    Subpillar serializers
    :return: All subpillar serializers
    :rtype: Object
    """

    class SubpillarListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('indicator_api:subpillar_detail', 'slug')

        class Meta:
            model = Subpillar
            fields = [
                'subpillar',
                'url',
            ]

    class SubpillarDetailSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        indicator_serializers = indicator_serializers()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        indicators = SerializerMethodField()

        class Meta:
            common_fields = [
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'indicators',
            ]
            model = Subpillar
            fields = [
                'id',
                'subpillar',
            ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_indicators(self, obj):
            """
            :param obj: Current record object
            :return: Indicator of a subpillar
            :rtype: Object/record
            """
            request = self.context['request']
            IndicatorListSerializer = self.indicator_serializers['IndicatorListSerializer']
            related_content = get_related_content(
                obj, IndicatorListSerializer, obj.indicator_relation, request
            )
            return related_content

    return {
        'SubpillarListSerializer': SubpillarListSerializer,
        'SubpillarDetailSerializer': SubpillarDetailSerializer
    }
