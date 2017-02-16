from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.experimentobject.experimentobjectserializers import experiment_object_serializers
from csacompendium.research.models import ObjectCategory
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content


def object_category_serializers():
    """
    Object category serializers
    :return: All object category serializers
    :rtype: Object
    """

    class ObjectCategoryListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:object_category_detail', 'slug')

        class Meta:
            model = ObjectCategory
            fields = [
                'object_category',
                'url',
            ]

    class ObjectCategoryDetailSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        experiment_object_serializers = experiment_object_serializers()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        experiment_object = SerializerMethodField()

        class Meta:
            common_fields = [
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'experiment_object',
            ]
            model = ObjectCategory
            fields = [
                'id',
                'object_category',
            ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_experiment_object(self, obj):
            """
            :param obj: Current record object
            :return: Experiment object
            :rtype: Object/record
            """
            request = self.context['request']
            ExperimentObjectListSerializer = self.experiment_object_serializers['ExperimentObjectListSerializer']
            related_content = get_related_content(
                obj, ExperimentObjectListSerializer, obj.experiment_object_relation, request
            )
            return related_content

    return {
        'ObjectCategoryListSerializer': ObjectCategoryListSerializer,
        'ObjectCategoryDetailSerializer': ObjectCategoryDetailSerializer
    }
