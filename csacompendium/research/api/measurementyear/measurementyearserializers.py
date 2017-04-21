from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.researchmeasurementyear.researchmeasurementyearserializers import \
    research_measurement_year_serializers
from csacompendium.research.models import MeasurementYear
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

research_measurement_year_serializers = research_measurement_year_serializers()


def measurement_year_serializers():
    """
    Measurement year serializers
    :return: All measurement year serializers
    :rtype: Object
    """
    class MeasurementYearBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = MeasurementYear
            fields = [
                'id',
                'measurement_year',
            ]

    class MeasurementYearRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        research_relation = SerializerMethodField()

        class Meta:
            model = MeasurementYear
            fields = [
                'research_relation',
            ]

    class MeasurementYearFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_research_relation(self, obj):
            """
            Gets research record
            :param obj: Current record object
            :return: Related research object/record
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchMeasurementYearContentTypeSerializer = research_measurement_year_serializers[
                'ResearchMeasurementYearContentTypeSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchMeasurementYearContentTypeSerializer,
                obj.research_measurement_year_relation, request
            )
            return related_content

    class MeasurementYearListSerializer(
        MeasurementYearBaseSerializer,
        MeasurementYearRelationBaseSerializer,
        MeasurementYearFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:measurement_year_detail', 'slug')

        class Meta:
            model = MeasurementYear
            fields =MeasurementYearBaseSerializer.Meta.fields + ['url', ] + \
                    MeasurementYearRelationBaseSerializer.Meta.fields

    class MeasurementYearDetailSerializer(
        MeasurementYearBaseSerializer,  MeasurementYearRelationBaseSerializer,
        FieldMethodSerializer, MeasurementYearFieldMethodSerializer
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
            ] + MeasurementYearRelationBaseSerializer.Meta.fields
            model = MeasurementYear
            fields = MeasurementYearBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'MeasurementYearListSerializer': MeasurementYearListSerializer,
        'MeasurementYearDetailSerializer': MeasurementYearDetailSerializer
    }
