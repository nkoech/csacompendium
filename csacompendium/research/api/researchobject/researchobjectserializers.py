from csacompendium.research.models import (
    ResearchObject,
    ExperimentObject,
)
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import (
    CreateSerializerUtil,
    get_related_content_url,
    FieldMethodSerializer
)
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)


def research_object_serializers():
    """
    Research object serializers
    :return: All research object serializers
    :rtype: Object
    """

    class ResearchObjectBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = ResearchObject
            fields = [
                'upper_soil_depth',
                'lower_soil_depth',
            ]

    def create_research_object_serializer(model_type=None, pk=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param pk: Primary key
        :param user: Record owner
        :return: Serializer class
        :rtype: Object
        """

        class ResearchObjectCreateSerializer(ResearchObjectBaseSerializer, CreateSerializerUtil):
            """
            Create a record
            """
            class Meta:
                model = ResearchObject
                fields = ['id', 'experimentobject', ] + \
                         ResearchObjectBaseSerializer.Meta.fields + \
                         ['last_update', 'time_created', ]

            def __init__(self, *args, **kwargs):
                super(ResearchObjectCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = pk
                self.user = user
                self.slugify = False
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Research object
                :rtype: Object
                """
                experimentobject = validated_data.get('experimentobject')
                upper_soil_depth = validated_data.get('upper_soil_depth')
                lower_soil_depth = validated_data.get('lower_soil_depth')
                research_object = ResearchObject.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    experimentobject=experimentobject,
                    upper_soil_depth=upper_soil_depth,
                    lower_soil_depth=lower_soil_depth,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if research_object:
                    return research_object
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return ResearchObjectCreateSerializer

    class ResearchObjectListSerializer(ResearchObjectBaseSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:research_object_detail', 'pk')

        class Meta:
            model = ResearchObject
            fields = ResearchObjectBaseSerializer.Meta.fields + ['url', ]

    class ResearchObjectDetailSerializer(ResearchObjectBaseSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        experiment_object_url = SerializerMethodField()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        content_type_url = SerializerMethodField()

        class Meta:
            common_fields = [
                'modified_by',
                'last_update',
                'time_created',
                'content_type_url',
            ]
            model = ResearchObject
            fields = ['id', 'experiment_object_url', ] + \
                     ResearchObjectBaseSerializer.Meta.fields + \
                     ['user', ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_experiment_object_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(ExperimentObject, obj.experimentobject.id)

    return {
        'create_research_object_serializer': create_research_object_serializer,
        'ResearchObjectListSerializer': ResearchObjectListSerializer,
        'ResearchObjectDetailSerializer': ResearchObjectDetailSerializer
    }
