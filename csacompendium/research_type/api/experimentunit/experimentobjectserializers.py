from csacompendium.research.models import (
    ExperimentObject,
    ObjectCategory,
)
from csacompendium.research.api.researchobject.researchobjectserializers import research_object_serializers
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import (
    FieldMethodSerializer,
    get_related_content,
    get_related_content_url
)
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)


def experiment_object_serializers():
    """
    Experiment object serializers
    :return: All experiment object serializers
    :rtype: Object
    """

    class ExperimentObjectBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = ExperimentObject
            fields = [
                'exp_object_code',
                'object_name',
                'latin_name',
            ]

    class ExperimentObjectListSerializer(ExperimentObjectBaseSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:experiment_object_detail', 'slug')

        class Meta:
            model = ExperimentObject
            fields = ExperimentObjectBaseSerializer.Meta.fields + ['url', ]

    class ExperimentObjectDetailSerializer(ExperimentObjectBaseSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        research_object_serializers = research_object_serializers()
        object_category_url = SerializerMethodField()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        research_object = SerializerMethodField()

        class Meta:
            common_fields = [
                'modified_by',
                'last_update',
                'time_created',
                'research_object',
            ]
            model = ExperimentObject
            fields = ['id', 'objectcategory', 'object_category_url', ] + \
                     ExperimentObjectBaseSerializer.Meta.fields + ['user', ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_object_category_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(ObjectCategory, obj.objectcategory.id)

        def get_research_object(self, obj):
            """
            :param obj: Current record object
            :return: Research object
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchObjectListSerializer = self.research_object_serializers['ResearchObjectListSerializer']
            related_content = get_related_content(
                obj, ResearchObjectListSerializer, obj.research_object_relation, request
            )
            return related_content

    return {
        'ExperimentObjectListSerializer': ExperimentObjectListSerializer,
        'ExperimentObjectDetailSerializer': ExperimentObjectDetailSerializer
    }
