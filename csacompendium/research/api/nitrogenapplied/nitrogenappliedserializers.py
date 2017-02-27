from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.controlresearch.controlresearchserializers import control_research_serializers
from csacompendium.research.api.treatmentresearch.treatmentresearchserializers import treatment_research_serializers
from csacompendium.research.models import NitrogenApplied
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content


def nitrogen_applied_serializers():
    """
    Nitrogen applied serializers
    :return: All nitrogen applied serializers
    :rtype: Object
    """

    class NitrogenAppliedListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:nitrogen_applied_detail', 'pk')

        class Meta:
            model = NitrogenApplied
            fields = [
                'nitrogen_amount',
                'amount_uom',
                'url',
            ]

    class NitrogenAppliedDetailSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        control_research_serializers = control_research_serializers()
        treatment_research_serializers = treatment_research_serializers()
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
            model = NitrogenApplied
            fields = [
                'id',
                'nitrogen_amount',
                'amount_uom',
            ] + common_fields
            read_only_fields = ['id', ] + common_fields

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
        'NitrogenAppliedListSerializer': NitrogenAppliedListSerializer,
        'NitrogenAppliedDetailSerializer': NitrogenAppliedDetailSerializer
    }
