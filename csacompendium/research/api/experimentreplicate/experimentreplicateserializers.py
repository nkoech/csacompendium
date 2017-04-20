from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.researchexperimentreplicate.researchexperimentreplicateserializers import \
    research_experiment_replicate_serializers
from csacompendium.research.models import ExperimentReplicate
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

research_experiment_replicate_serializers = research_experiment_replicate_serializers()


def experiment_replicate_serializers():
    """
    Experiment replicate serializers
    :return: All experiment replicate serializers
    :rtype: Object
    """
    class ExperimentReplicateBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = ExperimentReplicate
            fields = [
                'id',
                'no_replicate',
            ]

    class ExperimentReplicateRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        research_relation = SerializerMethodField()

        class Meta:
            model = ExperimentReplicate
            fields = [
                'research_relation',
            ]

    class ExperimentReplicateFieldMethodSerializer:
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
            ResearchExperimentReplicateContentTypeSerializer = research_experiment_replicate_serializers[
                'ResearchExperimentReplicateContentTypeSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchExperimentReplicateContentTypeSerializer,
                obj.research_experiment_replicate_relation, request
            )
            return related_content

    class ExperimentReplicateListSerializer(
        ExperimentReplicateBaseSerializer,
        ExperimentReplicateRelationBaseSerializer,
        ExperimentReplicateFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:experiment_replicate_detail', 'pk')

        class Meta:
            model = ExperimentReplicate
            fields =ExperimentReplicateBaseSerializer.Meta.fields + ['url', ] + \
                    ExperimentReplicateRelationBaseSerializer.Meta.fields

    class ExperimentReplicateDetailSerializer(
        ExperimentReplicateBaseSerializer,  ExperimentReplicateRelationBaseSerializer,
        FieldMethodSerializer,ExperimentReplicateFieldMethodSerializer
    ):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        research_relation = SerializerMethodField()

        class Meta:
            common_fields = [
                'user',
                'modified_by',
                'last_update',
                'time_created',
            ] + ExperimentReplicateRelationBaseSerializer.Meta.fields
            model = ExperimentReplicate
            fields = ExperimentReplicateBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'ExperimentReplicateListSerializer': ExperimentReplicateListSerializer,
        'ExperimentReplicateDetailSerializer': ExperimentReplicateDetailSerializer
    }
