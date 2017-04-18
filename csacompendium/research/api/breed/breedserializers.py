from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.researchexperimentunit.researchexperimentunitserializers import \
    research_experiment_unit_serializers
from csacompendium.research.models import Breed
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

research_experiment_unit_serializers = research_experiment_unit_serializers()


def breed_serializers():
    """
    Breed serializers
    :return: All breed serializers
    :rtype: Object
    """

    class BreedBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = Breed
            fields = [
                'id',
                'breed',
            ]

    class BreedRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        research_experiment_unit = SerializerMethodField()

        class Meta:
            model = Breed
            fields = [
                'research_experiment_unit',
            ]

    class BreedFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_research_experiment_unit(self, obj):
            """
            :param obj: Current record object
            :return: Research experiment unit object
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchExperimentUnitListSerializer = research_experiment_unit_serializers[
                'ResearchExperimentUnitListSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchExperimentUnitListSerializer, obj.research_experiment_unit_relation, request
            )
            return related_content

    class BreedListSerializer(
        BreedBaseSerializer,
        BreedRelationBaseSerializer,
        BreedFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:breed_detail', 'slug')

        class Meta:
            model = Breed
            fields = BreedBaseSerializer.Meta.fields + ['url', ] + \
                     BreedRelationBaseSerializer.Meta.fields

    class BreedDetailSerializer(
        BreedBaseSerializer, BreedRelationBaseSerializer,
        FieldMethodSerializer, BreedFieldMethodSerializer
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
            ] + BreedRelationBaseSerializer.Meta.fields
            model = Breed
            fields = BreedBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'BreedListSerializer': BreedListSerializer,
        'BreedDetailSerializer': BreedDetailSerializer
    }
