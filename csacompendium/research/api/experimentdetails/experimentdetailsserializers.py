from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.controlresearch.controlresearchserializers import control_research_serializers
from csacompendium.research.api.treatmentresearch.treatmentresearchserializers import treatment_research_serializers
from csacompendium.research.models import ExperimentDetails
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

control_research_serializers = control_research_serializers()
treatment_research_serializers = treatment_research_serializers()


def experiment_details_serializers():
    """
    Experiment details serializers
    :return: All experiment details serializers
    :rtype: Object
    """

    class AuthorFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
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

        def get_treatment_research(self, obj):
            """
            :param obj: Current record object
            :return: Treatment research object
            :rtype: Object/record
            """
            request = self.context['request']
            TreatmentResearchListSerializer = treatment_research_serializers['TreatmentResearchListSerializer']
            related_content = get_related_content(
                obj, TreatmentResearchListSerializer, obj.treatment_research_relation, request
            )
            return related_content

    class ExperimentDetailsListSerializer(ModelSerializer, AuthorFieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        control_research = SerializerMethodField()
        treatment_research = SerializerMethodField()
        url = hyperlinked_identity('research_api:experiment_details_detail', 'slug')

        class Meta:
            model = ExperimentDetails
            fields = [
                'exp_detail',
                'url',
                'control_research',
                'treatment_research',
            ]

    class ExperimentDetailsDetailSerializer(ModelSerializer, FieldMethodSerializer, AuthorFieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        control_research = SerializerMethodField()
        treatment_research = SerializerMethodField()

        class Meta:
            common_fields = [
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'control_research',
                'treatment_research',
            ]
            model = ExperimentDetails
            fields = [
                'id',
                'exp_detail',
            ] + common_fields
            read_only_fields = ['id', ] + common_fields

    return {
        'ExperimentDetailsListSerializer': ExperimentDetailsListSerializer,
        'ExperimentDetailsDetailSerializer': ExperimentDetailsDetailSerializer
    }
