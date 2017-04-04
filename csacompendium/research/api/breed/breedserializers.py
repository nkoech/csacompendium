from csacompendium.research.models import Breed
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import (
    CreateSerializerUtil,
    FieldMethodSerializer
)
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)


def breed_serializers():
    """
    Breed serializers
    :return: All breed serializers
    :rtype: Object
    """

    class BreedBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = Breed
            fields = [
                'id',
                'breed',
            ]

    class BreedRelationBaseSerializer(ModelSerializer):
        """
        Base relation serializer for DRY implementation.
        """
        content_type_url = SerializerMethodField()

        class Meta:
            model = Breed
            fields = [
                'content_type_url',
            ]

    def create_breed_serializer(model_type=None, slug=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param slug: slug
        :param user: Record owner
        :return: Serializer class
        :rtype: Object
        """

        class BreedCreateSerializer(BreedBaseSerializer, CreateSerializerUtil):
            """
            Create a record
            """

            class Meta:
                model = Breed
                fields = BreedBaseSerializer.Meta.fields + ['last_update', 'time_created', ]

            def __init__(self, *args, **kwargs):
                super(BreedCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = slug
                self.user = user
                self.slugify = True
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Breed object
                :rtype: Object
                """
                breed = validated_data.get('breed')
                breed = Breed.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    breed=breed,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if breed:
                    return breed
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return BreedCreateSerializer

    class BreedListSerializer(BreedBaseSerializer, BreedRelationBaseSerializer, FieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:breed_detail', 'slug')

        class Meta:
            model = Breed
            fields = BreedBaseSerializer.Meta.fields + ['url', ] + BreedRelationBaseSerializer.Meta.fields

    class BreedDetailSerializer(BreedBaseSerializer, BreedRelationBaseSerializer, FieldMethodSerializer):
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
            ] + BreedRelationBaseSerializer.Meta.fields
            model = Breed
            fields = BreedBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'create_breed_serializer': create_breed_serializer,
        'BreedListSerializer': BreedListSerializer,
        'BreedDetailSerializer': BreedDetailSerializer
    }
