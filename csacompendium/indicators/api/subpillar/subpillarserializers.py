from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.indicators.api.indicator.indicatorserializers import indicator_serializers
from csacompendium.indicators.models import Subpillar
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

indicator_serializers = indicator_serializers()


def subpillar_serializers():
    """
    Subpillar serializers
    :return: All subpillar serializers
    :rtype: Object
    """

    class SubpillarBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """

        class Meta:
            model = Subpillar
            fields = [
                'id',
                'subpillar',
            ]

    class SubpillarRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        indicators = SerializerMethodField()

        class Meta:
            model = Subpillar
            fields = [
                'indicators',
            ]

    class SubpillarFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_indicators(self, obj):
            """
            :param obj: Current record object
            :return: Indicator of a subpillar
            :rtype: Object/record
            """
            request = self.context['request']
            IndicatorListSerializer = indicator_serializers['IndicatorListSerializer']
            related_content = get_related_content(
                obj, IndicatorListSerializer, obj.indicator_relation, request
            )
            return related_content

    class SubpillarListSerializer(
        SubpillarBaseSerializer,
        SubpillarRelationBaseSerializer,
        SubpillarFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('indicator_outcome_api:subpillar_detail', 'slug')

        class Meta:
            model = Subpillar
            fields = SubpillarBaseSerializer.Meta.fields + ['url', ] + \
                     SubpillarRelationBaseSerializer.Meta.fields

    class SubpillarDetailSerializer(
        SubpillarBaseSerializer, SubpillarRelationBaseSerializer,
        FieldMethodSerializer, SubpillarFieldMethodSerializer):
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
            ] + SubpillarRelationBaseSerializer.Meta.fields
            model = Subpillar
            fields = SubpillarBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'SubpillarListSerializer': SubpillarListSerializer,
        'SubpillarDetailSerializer': SubpillarDetailSerializer
    }
