from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.controlresearch.controlresearchserializers import control_research_serializers
from csacompendium.research.models import MeasurementYear, MeasurementSeason
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import (
    FieldMethodSerializer,
    get_related_content,
    get_related_content_url,
)

control_research_serializers = control_research_serializers()


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
                'meas_year',
                'measurementseason',
            ]

    class MeasurementYearRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        measurement_season_url = SerializerMethodField()
        control_research = SerializerMethodField()

        class Meta:
            model = MeasurementYear
            fields = [
                'measurement_season_url',
                'control_research',
            ]

    class MeasurementYearFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """

        def get_measurement_season_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(MeasurementSeason, obj.measurementseason.id)

        def get_control_research(self, obj):
            """
            :param obj: Current record object
            :return: Control research object
            :rtype: Object/record
            """
            request = self.context['request']
            ControlResearchListSerializer = control_research_serializers['ControlResearchListSerializer']
            related_content = get_related_content(
                obj, ControlResearchListSerializer, obj.control_research_relation, request
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
            fields = MeasurementYearBaseSerializer.Meta.fields + ['url', ] + \
                     MeasurementYearRelationBaseSerializer.Meta.fields

    class MeasurementYearDetailSerializer(
        MeasurementYearBaseSerializer, MeasurementYearRelationBaseSerializer,
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
