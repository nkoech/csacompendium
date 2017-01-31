from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.csa_practice.api.csapractice.csapracticeserializers import csa_practice_serializers
from csacompendium.csa_practice.models import CsaTheme
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content


def csa_theme_serializers():
    """
    CSA theme serializers
    :return: All CSA theme serializers
    :rtype: Object
    """

    class CsaThemeListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('csa_practice_api:csa_theme_detail', 'slug')

        class Meta:
            model = CsaTheme
            fields = [
                'csa_theme',
                'url',
            ]

    class CsaThemeDetailSerializer(ModelSerializer, FieldMethodSerializer):
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
            model = CsaTheme
            fields = [
                'id',
                'csa_theme',
            ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_csa_practices(self, obj):
            """
            :param obj: Current record object
            :return: CSA practices of a CSA theme
            :rtype: Object/record
            """
            request = self.context['request']
            CsaPracticeListSerializer = self.csa_practice_serializers['CsaPracticeListSerializer']
            related_content = get_related_content(obj, CsaPracticeListSerializer, obj.csa_practice_relation, request)
            return related_content

    return {
        'CsaThemeListSerializer': CsaThemeListSerializer,
        'CsaThemeDetailSerializer': CsaThemeDetailSerializer
    }
