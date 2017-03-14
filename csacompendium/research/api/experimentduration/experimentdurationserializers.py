from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.research.researchserializers import research_serializers
from csacompendium.research.models import ExperimentDuration
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

research_serializers = research_serializers()


def experiment_duration_serializers():
    """
    Experiment duration serializers
    :return: All experiment duration serializers
    :rtype: Object
    """

    class ExperimentDurationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = ExperimentDuration
            fields = [
                'id',
                'exp_duration',
            ]

    class ExperimentDurationRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        research = SerializerMethodField()

        class Meta:
            model = ExperimentDuration
            fields = [
                'research',
            ]

    class ExperimentDurationFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_research(self, obj):
            """
            :param obj: Current record object
            :return: Research object
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchListSerializer = research_serializers['ResearchListSerializer']
            related_content = get_related_content(
                obj, ResearchListSerializer, obj.research_relation, request
            )
            return related_content

    class ExperimentDurationListSerializer(
        ExperimentDurationBaseSerializer,
        ExperimentDurationRelationBaseSerializer,
        ExperimentDurationFieldMethodSerializer,
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:experiment_duration_detail', 'pk')

        class Meta:
            model = ExperimentDuration
            fields = ExperimentDurationBaseSerializer.Meta.fields + ['url', ] + \
                     ExperimentDurationRelationBaseSerializer.Meta.fields

    class ExperimentDurationDetailSerializer(
        ExperimentDurationBaseSerializer, ExperimentDurationRelationBaseSerializer,
        FieldMethodSerializer, ExperimentDurationFieldMethodSerializer
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
            ] + ExperimentDurationRelationBaseSerializer.Meta.fields
            model = ExperimentDuration
            fields = ExperimentDurationBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'ExperimentDurationListSerializer': ExperimentDurationListSerializer,
        'ExperimentDurationDetailSerializer': ExperimentDurationDetailSerializer
    }
