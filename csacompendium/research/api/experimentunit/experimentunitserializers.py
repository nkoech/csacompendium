from csacompendium.research.api.breed.breedserializers import breed_serializers
from csacompendium.research.api.researchexperimentunit.researchexperimentunitserializers \
    import research_experiment_unit_serializers
from csacompendium.research.models import (
    ExperimentUnit,
    ExperimentUnitCategory,
)
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import (
    FieldMethodSerializer,
    get_related_content,
    get_related_content_url,
)
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)

breed_serializers = breed_serializers()
research_experiment_unit_serializers = research_experiment_unit_serializers()


def experiment_unit_serializers():
    """
    Experiment unit serializers
    :return: All experiment unit serializers
    :rtype: Object
    """

    class ExperimentUnitBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = ExperimentUnit
            fields = [
                'id',
                'exp_unit_code',
                'experimentunitcategory',
                'common_name',
                'latin_name',
            ]

    class ExperimentUnitRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        experiment_unit_category_url = SerializerMethodField()
        breeds = SerializerMethodField()
        research_relation = SerializerMethodField()

        class Meta:
            model = ExperimentUnit
            fields = [
                'experiment_unit_category_url',
                'breeds',
                'research_relation',
            ]

    class ExperimentUnitFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_experiment_unit_category_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            if obj.experimentunitcategory:
                return get_related_content_url(ExperimentUnitCategory, obj.experimentunitcategory.id)

        def get_breeds(self, obj):
            """
            Get related breed data
            :param obj: Current record object
            :return: Breed in an experiment unit/species
            :rtype: Object/record
            """
            request = self.context['request']
            BreedListSerializer = breed_serializers['BreedListSerializer']
            related_content = get_related_content(obj, BreedListSerializer, obj.breeds, request)
            return related_content

        def get_research_relation(self, obj):
            """
            Gets research record
            :param obj: Current record object
            :return: Related research object/record
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchExperimentUnitContentTypeSerializer = research_experiment_unit_serializers[
                'ResearchExperimentUnitContentTypeSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchExperimentUnitContentTypeSerializer, obj.research_experiment_unit_relation, request
            )
            return related_content

    class ExperimentUnitListSerializer(
        ExperimentUnitBaseSerializer,
        ExperimentUnitRelationBaseSerializer,
        ExperimentUnitFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:experiment_unit_detail', 'slug')

        class Meta:
            model = ExperimentUnit
            fields = ExperimentUnitBaseSerializer.Meta.fields + ['url', ] + \
                     ExperimentUnitRelationBaseSerializer.Meta.fields

    class ExperimentUnitDetailSerializer(
        ExperimentUnitBaseSerializer, ExperimentUnitRelationBaseSerializer,
        FieldMethodSerializer, ExperimentUnitFieldMethodSerializer
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
            ] + ExperimentUnitRelationBaseSerializer.Meta.fields
            model = ExperimentUnit
            fields = ExperimentUnitBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'ExperimentUnitListSerializer': ExperimentUnitListSerializer,
        'ExperimentUnitDetailSerializer': ExperimentUnitDetailSerializer
    }
