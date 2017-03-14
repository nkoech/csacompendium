from csacompendium.soils.api.serializers import soil_serializers
from csacompendium.locations.api.locationrelation.locationrelationserializer import location_relation_serializers
from csacompendium.research.api.serializers import research_serializers
from csacompendium.locations.models import Location
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import (
    CreateSerializerUtil,
    FieldMethodSerializer,
    get_related_content
)
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)

location_relation_serializers = location_relation_serializers()


def location_serializers():
    """
    Location serializers
    :return: All location serializers
    :rtype: Object
    """

    class LocationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = Location
            fields = [
                'id',
                'location_name',
                'latitude',
                'longitude',
                'elevation',
            ]

    class LocationRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        content_type_url = SerializerMethodField()
        relation_details = SerializerMethodField()
        soils = SerializerMethodField()
        research = SerializerMethodField()

        class Meta:
            model = Location
            fields = [
                'content_type_url',
                'relation_details',
                'soils',
                'research',
            ]

    class LocationFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_relation_details(self, obj):
            """
            Get related object type data
            :param obj: Current record object
            :return: Related content type
            :rtype: Object/record
            """
            request = self.context['request']
            LocationRelationContentTypeSerializer = location_relation_serializers[
                'LocationRelationContentTypeSerializer'
            ]
            related_content = get_related_content(
                obj, LocationRelationContentTypeSerializer, obj.location_relation_relation, request
            )
            return related_content

        def get_soils(self, obj):
            """
            Get related soil data
            :param obj: Current record object
            :return: Soils in a location
            :rtype: Object/record
            """
            request = self.context['request']
            SoilListSerializer = soil_serializers['SoilListSerializer']
            related_content = get_related_content(obj, SoilListSerializer, obj.soils, request)
            return related_content

        def get_research(self, obj):
            """
            :param obj: Current record object
            :return: Research object/record
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchListSerializer = research_serializers['ResearchListSerializer']
            related_content = get_related_content(
                obj, ResearchListSerializer, obj.research, request
            )
            return related_content

    def create_location_serializer(model_type=None, slug=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param slug: Hyphened slug
        :param user: Record owner
        :return: Serializer class
        :rtype: Object
        """

        class LocationCreateSerializer(LocationBaseSerializer, CreateSerializerUtil):
            """
            Create a record
            """
            class Meta:
                model = Location
                fields = LocationBaseSerializer.Meta.fields + ['last_update', 'time_created', ]

            def __init__(self, *args, **kwargs):
                super(LocationCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = slug
                self.user = user
                self.slugify = True
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Location object
                :rtype: Object
                """
                location_name = validated_data.get('location_name')
                latitude = validated_data.get('latitude')
                longitude = validated_data.get('longitude')
                elevation = validated_data.get('elevation')
                location = Location.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    location_name=location_name,
                    latitude=latitude,
                    longitude=longitude,
                    elevation=elevation,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if location:
                    return location
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return LocationCreateSerializer

    class LocationListSerializer(
        LocationBaseSerializer, LocationRelationBaseSerializer,
        FieldMethodSerializer, LocationFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('location_api:location_detail', 'slug')

        class Meta:
            model = Location
            fields = LocationBaseSerializer.Meta.fields + ['url', ] + \
                     LocationRelationBaseSerializer.Meta.fields

    class LocationDetailSerializer(
        LocationBaseSerializer, LocationRelationBaseSerializer,
        FieldMethodSerializer, LocationFieldMethodSerializer
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
            ] + LocationRelationBaseSerializer.Meta.fields
            model = Location
            fields = LocationBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'create_location_serializer': create_location_serializer,
        'LocationListSerializer': LocationListSerializer,
        'LocationDetailSerializer': LocationDetailSerializer
    }
