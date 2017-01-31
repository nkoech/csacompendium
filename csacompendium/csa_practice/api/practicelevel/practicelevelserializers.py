from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.csa_practice.api.csapractice.csapracticeserializers import csa_practice_serializers
from csacompendium.csa_practice.models import PracticeLevel
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content


def practice_level_serializers():
    """
    CSA practice level serializers
    :return: All CSA practice level serializers
    :rtype: Object
    """

    class PracticeLevelListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('csa_practice_api:practice_level_detail', 'slug')

        class Meta:
            model = PracticeLevel
            fields = [
                'practice_level',
                'url',
            ]

    class PracticeLevelDetailSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        csa_practice_serializers = csa_practice_serializers()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        csa_practices = SerializerMethodField()

        class Meta:
            common_fields = [
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'csa_practices',
            ]
            model = PracticeLevel
            fields = [
                'id',
                'practice_level',
            ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_csa_practices(self, obj):
            """
            :param obj: Current record object
            :return: CSA practices related to CSA practice level
            :rtype: Object/record
            """
            request = self.context['request']
            CsaPracticeListSerializer = self.csa_practice_serializers['CsaPracticeListSerializer']
            related_content = get_related_content(obj, CsaPracticeListSerializer, obj.csa_practice_relation, request)
            return related_content

    return {
        'PracticeLevelListSerializer': PracticeLevelListSerializer,
        'PracticeLevelDetailSerializer': PracticeLevelDetailSerializer
    }
