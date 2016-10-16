from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
# from csacompendium.research.api.researchspecies.researchspeciesserializer import research_species_serializers
from csacompendium.research.models import Species
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content


def species_serializers():
    """
    species serializers
    :return: All species serializers
    :rtype: Object
    """

    class SpeciesListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:species_detail', 'slug')

        class Meta:
            model = Species
            fields = [
                'id',
                'species',
                'url',
            ]

    class SpeciesDetailSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        # research_species_serializers = research_species_serializers()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        research_species = SerializerMethodField()

        class Meta:
            common_fields = [
                'research_species',
                'user',
                'modified_by',
                'last_update',
                'time_created',
            ]
            model = Species
            fields = [
                'id',
                'species',
            ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_research_species(self, obj):
            """
            :param obj: Current record object
            :return: Research species
            :rtype: Object/record
            """
            request = self.context['request']
            # ResearchSpeciesSerializer = self.research_species_serializers['ResearchSpeciesSerializer']
            # related_content = get_related_content(obj, ResearchSpeciesSerializer, obj.research_species, request)
            # return related_content

    return {
        'SpeciesListSerializer': SpeciesListSerializer,
        'SpeciesDetailSerializer': SpeciesDetailSerializer
    }
