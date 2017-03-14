from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.researchspecies.researchspeciesserializers import research_species_serializers
from csacompendium.research.models import Species
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

research_species_serializers = research_species_serializers()


def species_serializers():
    """
    Species serializers
    :return: All species serializers
    :rtype: Object
    """

    class SpeciesBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = Species
            fields = [
                'id',
                'species',
            ]

    class SpeciesRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        research_relation = SerializerMethodField()

        class Meta:
            model = Species
            fields = ['research_relation', ]

    class SpeciesFieldMethodSerializer:
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
            ResearchSpeciesContentTypeSerializer = research_species_serializers[
                'ResearchSpeciesContentTypeSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchSpeciesContentTypeSerializer, obj.research_species_relation, request
            )
            return related_content

    class SpeciesListSerializer(
        SpeciesBaseSerializer,
        SpeciesRelationBaseSerializer,
        SpeciesFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:species_detail', 'slug')

        class Meta:
            model = Species
            fields = SpeciesBaseSerializer.Meta.fields + ['url', ] + \
                     SpeciesRelationBaseSerializer.Meta.fields

    class SpeciesDetailSerializer(
        SpeciesBaseSerializer, SpeciesRelationBaseSerializer,
        FieldMethodSerializer, SpeciesFieldMethodSerializer
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
            ] + SpeciesRelationBaseSerializer.Meta.fields
            model = Species
            fields = SpeciesBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'SpeciesListSerializer': SpeciesListSerializer,
        'SpeciesDetailSerializer': SpeciesDetailSerializer
    }
