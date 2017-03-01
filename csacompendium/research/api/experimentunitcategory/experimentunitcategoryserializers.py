from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.experimentunit.experimentunitserializers import experiment_unit_serializers
from csacompendium.research.models import ExperimentUnitCategory
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

experiment_unit_serializers = experiment_unit_serializers()


def experiment_unit_category_serializers():
    """
    Experiment unit category serializers
    :return: All experiment unit category serializers
    :rtype: Object
    """

    class ExperimentUnitCategoryFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_experiment_units(self, obj):
            """
            Gets experiment unit(s) as parent record(s)
            :param obj: Current record object
            :return: Experiment unit related to experiment unit category
            :rtype: Object/record
            """
            request = self.context['request']
            ExperimentUnitListSerializer = experiment_unit_serializers['ExperimentUnitListSerializer']
            related_content = get_related_content(
                obj, ExperimentUnitListSerializer, obj.experiment_unit_relation, request
            )
            return related_content

    class ExperimentUnitCategoryListSerializer(ModelSerializer, ExperimentUnitCategoryFieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        experiment_units = SerializerMethodField()
        url = hyperlinked_identity('research_api:experiment_unit_category_detail', 'slug')

        class Meta:
            model = ExperimentUnitCategory
            fields = [
                'unit_category',
                'url',
                'experiment_units',
            ]

    class ExperimentUnitCategoryDetailSerializer(
        ModelSerializer, FieldMethodSerializer, ExperimentUnitCategoryFieldMethodSerializer
    ):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        experiment_units = SerializerMethodField()

        class Meta:
            common_fields = [
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'experiment_units',
            ]
            model = ExperimentUnitCategory
            fields = [
                'id',
                'unit_category',
            ] + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'ExperimentUnitCategoryListSerializer': ExperimentUnitCategoryListSerializer,
        'ExperimentUnitCategoryDetailSerializer': ExperimentUnitCategoryDetailSerializer
    }
