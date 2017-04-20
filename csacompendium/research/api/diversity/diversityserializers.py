from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.researchdiversity.researchdiversityserializers import \
    research_diversity_serializers
from csacompendium.research.models import Diversity
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

research_diversity_serializers = research_diversity_serializers()


def diversity_serializers():
    """
    Diversity serializers
    :return: All diversity serializers
    :rtype: Object
    """
    class DiversityBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = Diversity
            fields = [
                'id',
                'diversity',
            ]

    class DiversityRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        research_relation = SerializerMethodField()

        class Meta:
            model = Diversity
            fields = [
                'research_relation',
            ]

    class DiversityFieldMethodSerializer:
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
            ResearchDiversityContentTypeSerializer = research_diversity_serializers[
                'ResearchDiversityContentTypeSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchDiversityContentTypeSerializer,
                obj.research_diversity_relation, request
            )
            return related_content

    class DiversityListSerializer(
        DiversityBaseSerializer,
        DiversityRelationBaseSerializer,
        DiversityFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:diversity_detail', 'slug')

        class Meta:
            model = Diversity
            fields =DiversityBaseSerializer.Meta.fields + ['url', ] + \
                    DiversityRelationBaseSerializer.Meta.fields

    class DiversityDetailSerializer(
        DiversityBaseSerializer,  DiversityRelationBaseSerializer,
        FieldMethodSerializer, DiversityFieldMethodSerializer
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
            ] + DiversityRelationBaseSerializer.Meta.fields
            model = Diversity
            fields = DiversityBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'DiversityListSerializer': DiversityListSerializer,
        'DiversityDetailSerializer': DiversityDetailSerializer
    }
