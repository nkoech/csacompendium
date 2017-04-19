from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.indicators.api.researchoutcomeindicator.researchoutcomeindicatorserializers import \
    research_outcome_indicator_serializers
from csacompendium.indicators.models import ExperimentOutcome
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

research_outcome_indicator_serializers = research_outcome_indicator_serializers()


def experiment_outcome_serializers():
    """
    Experiment outcome serializers
    :return: All experiment outcome  serializers
    :rtype: Object
    """

    class ExperimentOutcomeBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = ExperimentOutcome
            fields = [
                'id',
                'mean_outcome',
                'std_outcome',
                'outcome_uom',
            ]

    class ExperimentOutcomeRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        research_outcome_indicator = SerializerMethodField()

        class Meta:
            model = ExperimentOutcome
            fields = [
                'research_outcome_indicator',
            ]

    class ExperimentOutcomeFieldMethodSerializer:
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

    class ExperimentOutcomeListSerializer(
        ExperimentOutcomeBaseSerializer,
        ExperimentOutcomeRelationBaseSerializer,
        ExperimentOutcomeFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('indicator_outcome_api:experiment_outcome_detail', 'pk')

        class Meta:
            model = ExperimentOutcome
            fields = ExperimentOutcomeBaseSerializer.Meta.fields + ['url', ] + \
                     ExperimentOutcomeRelationBaseSerializer.Meta.fields

    class ExperimentOutcomeDetailSerializer(
        ExperimentOutcomeBaseSerializer, ExperimentOutcomeRelationBaseSerializer,
        FieldMethodSerializer, ExperimentOutcomeFieldMethodSerializer
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
            ] + ExperimentOutcomeRelationBaseSerializer.Meta.fields
            model = ExperimentOutcome
            fields = ExperimentOutcomeBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'ExperimentOutcomeListSerializer': ExperimentOutcomeListSerializer,
        'ExperimentOutcomeDetailSerializer': ExperimentOutcomeDetailSerializer
    }
