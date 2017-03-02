from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.csa_practice.api.csapractice.csapracticeserializers import csa_practice_serializers
from csacompendium.csa_practice.models import CsaTheme
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

csa_practice_serializers = csa_practice_serializers()


def csa_theme_serializers():
    """
    CSA theme serializers
    :return: All CSA theme serializers
    :rtype: Object
    """

    class CsaThemeBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = CsaTheme
            fields = [
                'id',
                'csa_theme',
            ]

    class CsaThemeRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        csa_practices = SerializerMethodField()

        class Meta:
            model = CsaTheme
            fields = [
                'csa_practices',
            ]

    class CsaThemeFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_csa_practices(self, obj):
            """
            :param obj: Current record object
            :return: CSA practices of a CSA theme
            :rtype: Object/record
            """
            request = self.context['request']
            CsaPracticeListSerializer = csa_practice_serializers['CsaPracticeListSerializer']
            related_content = get_related_content(obj, CsaPracticeListSerializer, obj.csa_practice_relation, request)
            return related_content

    class CsaThemeListSerializer(
        CsaThemeBaseSerializer,
        CsaThemeRelationBaseSerializer,
        CsaThemeFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('csa_practice_api:csa_theme_detail', 'slug')

        class Meta:
            model = CsaTheme
            fields = CsaThemeBaseSerializer.Meta.fields + ['url', ] + \
                     CsaThemeRelationBaseSerializer.Meta.fields

    class CsaThemeDetailSerializer(
        CsaThemeBaseSerializer, CsaThemeRelationBaseSerializer,
        FieldMethodSerializer, CsaThemeFieldMethodSerializer
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
            ] + CsaThemeRelationBaseSerializer.Meta.fields
            model = CsaTheme
            fields = CsaThemeBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'CsaThemeListSerializer': CsaThemeListSerializer,
        'CsaThemeDetailSerializer': CsaThemeDetailSerializer
    }
