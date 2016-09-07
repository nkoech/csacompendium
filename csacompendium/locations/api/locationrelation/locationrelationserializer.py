from csacompendium.locations.models import Location, LocationRelation
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)


def location_relation_serializers():
    """
    LocationRelation serializers
    :return: All location serializers
    :rtype: Object
    """

    def create_location_relation_serializer(model_type=None, pk=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param pk: Primary key
        :param user: Object owner
        :return: Serializer class
        :rtype: Object
        """

        class LocationRelationCreateSerializer(ModelSerializer):
            """
            Create a record
            """
            user = SerializerMethodField()
            modified_by = SerializerMethodField()

            class Meta:
                model = LocationRelation
                fields = [
                    'id',
                    'location',
                    'user',
                    'modified_by',
                    'last_update',
                    'time_created',
                ]
                read_only_fields = [
                    'user',
                    'modified_by',
                ]

            def get_user(self, obj):
                """
                :param obj: Current record object
                :return: Name of user who created the record
                :rtype: String
                """
                return str(obj.user.username)

            def get_modified_by(self, obj):
                """
                :param obj: Current record object
                :return: Name of user who edited a record
                :rtype: String
                """
                return str(obj.modified_by.username)

            def __init__(self, *args, **kwargs):
                self.model_type = model_type
                self.pk = pk
                self.user = self.get_authenticated_user()
                return super(LocationRelationCreateSerializer, self).__init__(*args, **kwargs)

            def get_authenticated_user(self):
                """
                Get an authenticated user
                :return: Authenticated user
                :rtype: User object
                """
                if user:
                    auth_user = user
                else:
                    User_model = get_user_model()
                    auth_user = User_model.objects.all().first()
                return auth_user

            def validate(self, data):
                """
                Validates data
                :param data: Input data
                :return: Validated data
                :rtype: Object
                """
                model_type = self.model_type
                model_qs = ContentType.objects.filter(model=model_type)
                if not model_qs.exists() or model_qs.count() != 1:
                    raise ValidationError('This is not a valid content type')
                any_model = model_qs.first().model_class()
                obj_qs = any_model.objects.filter(pk=self.pk)
                if not obj_qs.exists() or obj_qs.count() != 1:
                    raise ValidationError('This is not a primary key for this content type')
                return data

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Location object
                :rtype: Object
                """
                location = validated_data.get('location')
                location_relation = LocationRelation.objects.create_by_model_type(
                    self.model_type, self.pk, location, self.user
                )
                return location_relation

        return LocationRelationCreateSerializer

    class LocationRelationListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        location_url = SerializerMethodField()
        content_type_url = SerializerMethodField()
        location_relation_url = hyperlinked_identity('location_api:locationrelation_detail', 'pk')

        class Meta:
            model = LocationRelation
            fields = [
                'id',
                'location',
                'location_url',
                'content_type_url',
                'location_relation_url',
            ]

        def get_location_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            try:
                location_obj = Location.objects.get(id=obj.location.id)
                return location_obj.get_api_url()
            except:
                return None

        def get_content_type_url(self, obj):
                """
                Get related content type/object url
                :param obj: Current record object
                :return: URL to related object
                :rtype: String
                """
                try:
                    return obj.content_object.get_api_url()
                except:
                    return None

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
            try:
                location_obj = Location.objects.get(id=obj.location.id)
                return location_obj.get_api_url()
            except:
                return None

        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Name of the location
            :rtype: String
            """
            return obj.id

    class LocationRelationContentTypeSerializer(ModelSerializer):
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
            :return: Name of the location
            :rtype: String
            """
            return obj.id

        def get_content_type_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            try:
                return obj.content_object.get_api_url()
            except:
                return None

    class LocationRelationDetailSerializer(ModelSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        location_url = SerializerMethodField()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        content_type_url = SerializerMethodField()

        class Meta:
            model = LocationRelation
            fields = [
                'id',
                'location',
                'location_url',
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'content_type_url',
            ]
            read_only_fields = [
                'id',
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'location_url',
                'content_type_url',
            ]

        def get_location_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            try:
                location_obj = Location.objects.get(id=obj.location.id)
                return location_obj.get_api_url()
            except:
                return None

        def get_user(self, obj):
            """
            :param obj: Current record object
            :return: Name of user who created the record
            :rtype: String
            """
            return str(obj.user.username)

        def get_modified_by(self, obj):
            """
            :param obj: Current record object
            :return: Name of user who edited a record
            :rtype: String
            """
            return str(obj.modified_by.username)

        def get_content_type_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            try:
                return obj.content_object.get_api_url()
            except:
                return None

    return create_location_relation_serializer, LocationRelationListSerializer, \
           LocationRelationSerializer, LocationRelationContentTypeSerializer, LocationRelationDetailSerializer
