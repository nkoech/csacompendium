from rest_framework.serializers import ModelSerializer
from csacompendium.csa_practice.api.csapractice.csapracticeserializers import csa_practice_serializers
from csacompendium.csa_practice.api.practicelevel.practicelevelserializers import practice_level_serializers
from django.contrib.auth.models import User

csa_practice_serializers = csa_practice_serializers()


def global_search_serializers():
    """
    Global search serializers
    :return: All global search serializers
    :rtype: Object
    """

    class GlobalSearchListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """

        class Meta:
            model = None
            # model = CsaPractice

        # def to_native(self, obj):
        #     if isinstance(obj, obj.__class__):
        #         CsaPracticeListSerializer = csa_practice_serializers['CsaPracticeListSerializer']
        #         serializer = CsaPracticeListSerializer(obj)
        #     else:
        #         raise Exception("Neither a Snippet nor User instance!")
        #     return serializer.data

    return {
        'GlobalSearchListSerializer': GlobalSearchListSerializer
    }
