from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.researchmeasurementyear.researchmeasurementyearserializers import \
    research_measurement_year_serializers
from csacompendium.research.models import MeasurementDuration
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

research_measurement_year_serializers = research_measurement_year_serializers()


def measurement_duration_serializers():
    """
    Measurement duration serializers
    :return: All measurement duration serializers
    :rtype: Object
    """

    class MeasurementDurationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = MeasurementDuration
            fields = [
                'id',
                'measurement_duration',
            ]

    class MeasurementDurationRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        research_measurement_year = SerializerMethodField()

        class Meta:
            model = MeasurementDuration
            fields = [
                'research_measurement_year',
            ]

    class MeasurementDurationFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_research_measurement_year(self, obj):
            """
            :param obj: Current record object
            :return: Research measurement year object
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchMeasurementYearListSerializer = research_measurement_year_serializers[
                'ResearchMeasurementYearListSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchMeasurementYearListSerializer, obj.research_measurement_year_relation, request
            )
            return related_content

    class MeasurementDurationListSerializer(
        MeasurementDurationBaseSerializer,
        MeasurementDurationRelationBaseSerializer,
        MeasurementDurationFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:measurement_duration_detail', 'pk')

        class Meta:
            model = MeasurementDuration
            fields = MeasurementDurationBaseSerializer.Meta.fields + ['url', ] + \
                     MeasurementDurationRelationBaseSerializer.Meta.fields

    class MeasurementDurationDetailSerializer(
        MeasurementDurationBaseSerializer, MeasurementDurationRelationBaseSerializer,
        FieldMethodSerializer, MeasurementDurationFieldMethodSerializer
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
            ] + MeasurementDurationRelationBaseSerializer.Meta.fields
            model = MeasurementDuration
            fields = MeasurementDurationBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'MeasurementDurationListSerializer': MeasurementDurationListSerializer,
        'MeasurementDurationDetailSerializer': MeasurementDurationDetailSerializer
    }
