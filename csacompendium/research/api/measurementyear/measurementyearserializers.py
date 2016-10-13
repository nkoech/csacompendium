from csacompendium.research.models import (
    MeasurementYear,
    MeasurementSeason,
)
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import CreateSerializerUtil
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)


def measurement_year_serializers():
    """
    Measurement year serializers
    :return: All measurement year serializers
    :rtype: Object
    """

    class MeasurementYearBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = MeasurementYear
            fields = [
                'meas_year',
            ]

    def create_measurement_year_serializer(model_type=None, pk=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param pk: Primary key
        :param user: Record owner
        :return: Serializer class
        :rtype: Object
        """

        class MeasurementYearCreateSerializer(MeasurementYearBaseSerializer, CreateSerializerUtil):
            """
            Create a record
            """

            class Meta:
                model = MeasurementYear
                fields = ['id', ] + \
                         MeasurementYearBaseSerializer.Meta.fields + \
                         ['measurementseason', 'last_update', 'time_created', ]

            def __init__(self, *args, **kwargs):
                super(MeasurementYearCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = pk
                self.user = user
                self.slugify = False
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Measurement year object
                :rtype: Object
                """
                meas_year = validated_data.get('meas_year')
                measurementseason = validated_data.get('measurementseason')
                measurement_year = MeasurementYear.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    meas_year=meas_year,
                    measurementseason=measurementseason,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if measurement_year:
                    return measurement_year
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return MeasurementYearCreateSerializer

    class MeasurementYearListSerializer(MeasurementYearBaseSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:measurement_year_detail', 'pk')

        class Meta:
            model = MeasurementYear
            fields = MeasurementYearBaseSerializer.Meta.fields + ['url', ]

    class MeasurementYearDetailSerializer(MeasurementYearBaseSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        measurement_season_url = SerializerMethodField()
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
            model = MeasurementYear
            fields = ['id', ] + \
                     MeasurementYearBaseSerializer.Meta.fields + ['measurement_season_url', 'user', ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_measurement_season_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            try:
                measurementseason_obj = MeasurementSeason.objects.get(id=obj.measurementseason.id)
                return measurementseason_obj.get_api_url()
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

    return {
        'create_measurement_year_serializer': create_measurement_year_serializer,
        'MeasurementYearListSerializer': MeasurementYearListSerializer,
        'MeasurementYearDetailSerializer': MeasurementYearDetailSerializer
    }
