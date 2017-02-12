from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research_type.api.controlresearch.controlresearchserializers import control_research_serializers
from csacompendium.research_type.api.treatmentresearch.treatmentresearchserializers import treatment_research_serializers
from csacompendium.research_type.models import MeasurementYear, MeasurementSeason
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import (
    FieldMethodSerializer,
    get_related_content,
    get_related_content_url,
)


def measurement_year_serializers():
    """
    Measurement year serializers
    :return: All measurement year serializers
    :rtype: Object
    """

    class MeasurementYearListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_type_api:measurement_year_detail', 'slug')

        class Meta:
            model = MeasurementYear
            fields = [
                'meas_year',
                'url',
            ]

    class MeasurementYearDetailSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        control_research_serializers = control_research_serializers()
        treatment_research_serializers = treatment_research_serializers()
        measurement_season_url = SerializerMethodField()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        control_research = SerializerMethodField()
        treatment_research = SerializerMethodField()

        class Meta:
            common_fields = [
                'measurement_season_url',
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'control_research',
                'treatment_research',
            ]
            model = MeasurementYear
            fields = [
                'id',
                'meas_year',
                'measurementseason',
            ] + common_fields
            read_only_fields = ['id', ] + common_fields

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
            ControlResearchListSerializer = self.control_research_serializers['ControlResearchListSerializer']
            related_content = get_related_content(
                obj, ControlResearchListSerializer, obj.control_research_relation, request
            )
            return related_content

        def get_treatment_research(self, obj):
            """
            :param obj: Current record object
            :return: Treatment research object
            :rtype: Object/record
            """
            request = self.context['request']
            TreatmentResearchListSerializer = self.treatment_research_serializers['TreatmentResearchListSerializer']
            related_content = get_related_content(
                obj, TreatmentResearchListSerializer, obj.treatment_research_relation, request
            )
            return related_content

    return {
        'MeasurementYearListSerializer': MeasurementYearListSerializer,
        'MeasurementYearDetailSerializer': MeasurementYearDetailSerializer
    }
