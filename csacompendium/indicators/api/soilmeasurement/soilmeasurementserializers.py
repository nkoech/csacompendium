from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.indicators.api.researchoutcomeindicator.researchoutcomeindicatorserializers import \
    research_outcome_indicator_serializers
from csacompendium.indicators.models import SoilMeasurement
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

research_outcome_indicator_serializers = research_outcome_indicator_serializers()


def soil_measurement_serializers():
    """
    Soil measurement serializers
    :return: All soil measurement  serializers
    :rtype: Object
    """

    class SoilMeasurementBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = SoilMeasurement
            fields = [
                'id',
                'upper_soil_depth',
                'lower_soil_depth',
                'depth_uom',
                'incubation_days',
            ]

    class SoilMeasurementRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        research_outcome_indicator = SerializerMethodField()

        class Meta:
            model = SoilMeasurement
            fields = [
                'research_outcome_indicator',
            ]

    class SoilMeasurementFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_research_outcome_indicator(self, obj):
            """
            :param obj: Current record object
            :return: Research outcome indicator object
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchOutcomeIndicatorListSerializer = research_outcome_indicator_serializers[
                'ResearchOutcomeIndicatorListSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchOutcomeIndicatorListSerializer, obj.research_outcome_indicator_relation, request
            )
            return related_content

    class SoilMeasurementListSerializer(
        SoilMeasurementBaseSerializer,
        SoilMeasurementRelationBaseSerializer,
        SoilMeasurementFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('indicator_outcome_api:soil_measurement_detail', 'pk')

        class Meta:
            model = SoilMeasurement
            fields = SoilMeasurementBaseSerializer.Meta.fields + ['url', ] + \
                     SoilMeasurementRelationBaseSerializer.Meta.fields

    class SoilMeasurementDetailSerializer(
        SoilMeasurementBaseSerializer, SoilMeasurementRelationBaseSerializer,
        FieldMethodSerializer, SoilMeasurementFieldMethodSerializer
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
            ] + SoilMeasurementRelationBaseSerializer.Meta.fields
            model = SoilMeasurement
            fields = SoilMeasurementBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'SoilMeasurementListSerializer': SoilMeasurementListSerializer,
        'SoilMeasurementDetailSerializer': SoilMeasurementDetailSerializer
    }
