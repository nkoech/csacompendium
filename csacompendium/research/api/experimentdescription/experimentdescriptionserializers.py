from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.researchexperimentdescription.researchexperimentdescriptionserializers import \
    research_experiment_description_serializers
from csacompendium.research.models import ExperimentDescription
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

research_experiment_description_serializers = research_experiment_description_serializers()


def experiment_description_serializers():
    """
    Experiment description serializers
    :return: All experiment description serializers
    :rtype: Object
    """
    class ExperimentDescriptionBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = ExperimentDescription
            fields = [
                'id',
                'experiment_description',
            ]

    class ExperimentDescriptionRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        research_relation = SerializerMethodField()

        class Meta:
            model = ExperimentDescription
            fields = [
                'research_relation',
            ]

    class ExperimentDescriptionFieldMethodSerializer:
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
            ResearchExperimentDescriptionContentTypeSerializer = research_experiment_description_serializers[
                'ResearchExperimentDescriptionContentTypeSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchExperimentDescriptionContentTypeSerializer,
                obj.research_experiment_description_relation, request
            )
            return related_content

    class ExperimentDescriptionListSerializer(
        ExperimentDescriptionBaseSerializer,
        ExperimentDescriptionRelationBaseSerializer,
        ExperimentDescriptionFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:experiment_description_detail', 'slug')

        class Meta:
            model = ExperimentDescription
            fields =ExperimentDescriptionBaseSerializer.Meta.fields + ['url', ] + \
                    ExperimentDescriptionRelationBaseSerializer.Meta.fields

    class ExperimentDescriptionDetailSerializer(
        ExperimentDescriptionBaseSerializer,  ExperimentDescriptionRelationBaseSerializer,
        FieldMethodSerializer, ExperimentDescriptionFieldMethodSerializer
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
            ] + ExperimentDescriptionRelationBaseSerializer.Meta.fields
            model = ExperimentDescription
            fields = ExperimentDescriptionBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'ExperimentDescriptionListSerializer': ExperimentDescriptionListSerializer,
        'ExperimentDescriptionDetailSerializer': ExperimentDescriptionDetailSerializer
    }
