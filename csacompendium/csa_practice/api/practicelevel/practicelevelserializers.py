from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.csa_practice.api.csapractice.csapracticeserializers import csa_practice_serializers
from csacompendium.csa_practice.models import PracticeLevel
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

csa_practice_serializers = csa_practice_serializers()

def practice_level_serializers():
    """
    CSA practice level serializers
    :return: All CSA practice level serializers
    :rtype: Object
    """

    class PracticeLevelBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = PracticeLevel
            fields = [
                'id',
                'practice_level',
            ]

    class PracticeLevelRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        csa_practices = SerializerMethodField()

        class Meta:
            model = PracticeLevel
            fields = [
                'csa_practices',
            ]

    class PracticeLevelFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_csa_practices(self, obj):
            """
            :param obj: Current record object
            :return: CSA practices related to CSA practice level
            :rtype: Object/record
            """
            request = self.context['request']
            CsaPracticeListSerializer = csa_practice_serializers['CsaPracticeListSerializer']
            related_content = get_related_content(obj, CsaPracticeListSerializer, obj.csa_practice_relation, request)
            return related_content

    class PracticeLevelListSerializer(
        PracticeLevelBaseSerializer,
        PracticeLevelRelationBaseSerializer,
        PracticeLevelFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('csa_practice_api:practice_level_detail', 'slug')

        class Meta:
            model = PracticeLevel
            fields = PracticeLevelBaseSerializer.Meta.fields + ['url', ] + \
                     PracticeLevelRelationBaseSerializer.Meta.fields

    class PracticeLevelDetailSerializer(
        PracticeLevelBaseSerializer, PracticeLevelRelationBaseSerializer,
        FieldMethodSerializer, PracticeLevelFieldMethodSerializer
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
            ] + PracticeLevelRelationBaseSerializer.Meta.fields
            model = PracticeLevel
            fields = PracticeLevelBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'PracticeLevelListSerializer': PracticeLevelListSerializer,
        'PracticeLevelDetailSerializer': PracticeLevelDetailSerializer
    }
