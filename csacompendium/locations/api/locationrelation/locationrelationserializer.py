from csacompendium.locations.models import Location, LocationRelation
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


def location_relation_serializers():
    """
    LocationsRelation serializers
    :return: All location relation serializers
    :rtype: Object
    """

    class LocationRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = LocationRelation
            fields = [
                'id',
                'location',
            ]

    class LocationRelationRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        content_type_url = SerializerMethodField()
        location_url = SerializerMethodField()

        class Meta:
            model = LocationRelation
            fields = [
                'content_type_url',
                'location_url',
            ]

    class LocationRelationFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_location_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(Location, obj.location.id)

    def create_location_relation_serializer(model_type=None, pk=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param pk: Primary key
        :param user: Object owner
        :return: Serializer class
        :rtype: Object
        """

        class LocationRelationCreateSerializer(LocationRelationBaseSerializer, CreateSerializerUtil):
            """
            Create a record
            """
            class Meta:
                model = LocationRelation
                fields = LocationRelationBaseSerializer.Meta.fields + ['last_update', 'time_created', ]

            def __init__(self, *args, **kwargs):
                super(LocationRelationCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = pk
                self.user = user
                self.slugify = False
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Location relation object
                :rtype: Object
                """
                location = validated_data.get('location')
                location_relation = LocationRelation.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    location=location,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if location_relation:
                    return location_relation
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return LocationRelationCreateSerializer

    class LocationRelationListSerializer(
        LocationRelationBaseSerializer, LocationRelationRelationBaseSerializer,
        FieldMethodSerializer, LocationRelationFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        location_relation_url = hyperlinked_identity('location_api:locationrelation_detail', 'pk')

        class Meta:
            model = LocationRelation
            fields = LocationRelationBaseSerializer.Meta.fields + ['location_relation_url', ] + \
                     LocationRelationRelationBaseSerializer.Meta.fields

    class LocationRelationSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        location_url = SerializerMethodField()
        relation_id = SerializerMethodField()
        location_relation_url = hyperlinked_identity('location_api:locationrelation_detail', 'pk')

        class Meta:
            model = LocationRelation
            fields = [
                'relation_id',
                'location_id',
                'location_url',
                'location_relation_url',
            ]

        def get_location_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(Location, obj.location.id)

        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Location relation id
            :rtype: Integer
            """
            return obj.id

    class LocationRelationContentTypeSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        relation_id = SerializerMethodField()
        content_type_url = SerializerMethodField()
        location_relation_url = hyperlinked_identity('location_api:locationrelation_detail', 'pk')

        class Meta:
            model = LocationRelation
            fields = [
                'relation_id',
                'object_id',
                'content_type_url',
                'location_relation_url',
            ]

        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Relation id
            :rtype: String
            """
            return obj.id

    class LocationRelationDetailSerializer(
        LocationRelationBaseSerializer, LocationRelationRelationBaseSerializer,
        FieldMethodSerializer, LocationRelationFieldMethodSerializer
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
            ] + LocationRelationRelationBaseSerializer.Meta.fields

            model = LocationRelation
            fields = LocationRelationBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'create_location_relation_serializer': create_location_relation_serializer,
        'LocationRelationListSerializer': LocationRelationListSerializer,
        'LocationRelationSerializer': LocationRelationSerializer,
        'LocationRelationContentTypeSerializer': LocationRelationContentTypeSerializer,
        'LocationRelationDetailSerializer': LocationRelationDetailSerializer
    }
