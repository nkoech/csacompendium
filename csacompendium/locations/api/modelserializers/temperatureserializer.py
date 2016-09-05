from csacompendium.locations.models import Temperature
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)


def temperature_serializers():
    """
    Temperature serializers
    :return: All temperature serializers
    :rtype: Object
    """