from csacompendium.locations.models import LocationRelation
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

    # def create_location_serializer(model_type='country', slug=None, user=None):
    #     """
    #     Creates a model serializer
    #     :param model_type: Model
    #     :param slug: Hyphened slug
    #     :param user: Record owner
    #     :return: Serializer class
    #     :rtype: Object
    #     """
    #
    #     class LocationCreateSerializer(ModelSerializer):
    #         """
    #         Create a record
    #         """
    #
    #         class Meta:
    #             model = Location
    #             fields = [
    #                 'id',
    #                 'location_name',
    #                 'latitude',
    #                 'longitude',
    #                 'elevation',
    #                 'last_update',
    #                 'time_created',
    #             ]
    #
    #         def __init__(self, *args, **kwargs):
    #             self.model_type = model_type
    #             self.slug = slug
    #             self.user = self.get_authenticated_user()
    #             return super(LocationCreateSerializer, self).__init__(*args, **kwargs)
    #
    #         def get_authenticated_user(self):
    #             """
    #             Get an authenticated user
    #             :return: Authenticated user
    #             :rtype: User object
    #             """
    #             if user:
    #                 auth_user = user
    #             else:
    #                 User_model = get_user_model()
    #                 auth_user = User_model.objects.all().first()
    #             return auth_user
    #
    #         def validate(self, data):
    #             """
    #             Validates data
    #             :param data: Input data
    #             :return: Validated data
    #             :rtype: Object
    #             """
    #             model_type = self.model_type
    #             model_qs = ContentType.objects.filter(model=model_type)
    #             if not model_qs.exists() or model_qs.count() != 1:
    #                 raise ValidationError('This is not a valid content type')
    #             any_model = model_qs.first().model_class()
    #             obj_qs = any_model.objects.filter(slug=self.slug)
    #             if not obj_qs.exists() or obj_qs.count() != 1:
    #                 raise ValidationError('This is not a slug for this content type')
    #             return data
    #
    #         def create(self, validated_data):
    #             """
    #             Created record from validated data
    #             :param validated_data: Validated data
    #             :return: Location object
    #             :rtype: Object
    #             """
    #             location_name = validated_data.get('location_name')
    #             latitude = validated_data.get('latitude')
    #             longitude = validated_data.get('longitude')
    #             elevation = validated_data.get('elevation')
    #             location = Location.objects.create_by_model_type(
    #                 self.model_type, self.slug, location_name, latitude, longitude, elevation, self.user
    #             )
    #             return location
    #
    #     return LocationCreateSerializer

    class LocationRelationListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        # url = hyperlinked_identity('location_api:location_detail', 'slug')

        class Meta:
            model = LocationRelation
            fields = [
                'location',
                # 'url',
            ]

    # class LocationDetailSerializer(ModelSerializer):
    #     """
    #     Serialize single record into an API. This is dependent on fields given.
    #     """
    #     user = SerializerMethodField()
    #     modified_by = SerializerMethodField()
    #     content_type_url = SerializerMethodField()
    #
    #     class Meta:
    #         model = Location
    #         fields = [
    #             'id',
    #             'location_name',
    #             'latitude',
    #             'longitude',
    #             'elevation',
    #             'user',
    #             'modified_by',
    #             'last_update',
    #             'time_created',
    #             'content_type_url',
    #         ]
    #         read_only_fields = [
    #             'id',
    #             'user',
    #             'modified_by',
    #             'last_update',
    #             'time_created',
    #             'content_type_url',
    #         ]
    #
    #     def get_user(self, obj):
    #         """
    #         :param obj: Current record object
    #         :return: Name of user who created the record
    #         :rtype: String
    #         """
    #         return str(obj.user.username)
    #
    #     def get_modified_by(self, obj):
    #         """
    #         :param obj: Current record object
    #         :return: Name of user who edited a record
    #         :rtype: String
    #         """
    #         return str(obj.modified_by.username)
    #
    #     def get_content_type_url(self, obj):
    #         """
    #         Get related content type/object url
    #         :param obj: Current record object
    #         :return: URL to related object
    #         :rtype: String
    #         """
    #         try:
    #             return obj.content_object.get_api_url()
    #         except:
    #             return None

    return LocationRelationListSerializer
