from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.csa_practice.api.csapractice.csapracticeserializers import csa_practice_serializers
from csacompendium.csa_practice.models import PracticeType
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

csa_practice_serializers = csa_practice_serializers()


def practice_type_serializers():
    """
    CSA practice type serializers
    :return: All CSA practice type serializers
    :rtype: Object
    """

    class PracticeTypeBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = PracticeType
            fields = [
                'id',
                'practice_type',
            ]

    class PracticeTypeRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        csa_practices = SerializerMethodField()

        class Meta:
            model = PracticeType
            fields = [
                'csa_practices',
            ]

    class PracticeTypeFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """

        def get_csa_practices(self, obj):
            """
            :param obj: Current record object
            :return: CSA practices related to CSA practice category
            :rtype: Object/record
            """
            request = self.context['request']
            CsaPracticeListSerializer = csa_practice_serializers['CsaPracticeListSerializer']
            related_content = get_related_content(obj, CsaPracticeListSerializer, obj.csa_practice_relation, request)
            return related_content

    class PracticeTypeListSerializer(
        PracticeTypeBaseSerializer,
        PracticeTypeRelationBaseSerializer,
        PracticeTypeFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('csa_practice_api:practice_type_detail', 'slug')

        class Meta:
            model = PracticeType
            fields = PracticeTypeBaseSerializer.Meta.fields + ['url', ] + \
                     PracticeTypeRelationBaseSerializer.Meta.fields

    class PracticeTypeDetailSerializer(
        PracticeTypeBaseSerializer, PracticeTypeRelationBaseSerializer,
        FieldMethodSerializer, PracticeTypeFieldMethodSerializer
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
            ] + PracticeTypeRelationBaseSerializer.Meta.fields
            model = PracticeType
            fields = PracticeTypeBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'PracticeTypeListSerializer': PracticeTypeListSerializer,
        'PracticeTypeDetailSerializer': PracticeTypeDetailSerializer
    }
