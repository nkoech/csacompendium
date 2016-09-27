from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import ValidationError


class CreateSerializerUtil:
    """
    Utility class that would create a serializer class
    """

    def __init__(self):
        self.model_type = None
        self.key = None
        self.user = None
        self.slugify = None
        self.auth_user = None

    def get_authenticated_user(self, user):
        """
        Get an authenticated user
        :param user: Record owner/creator
        :return: Authenticated user
        :rtype: User object
        """
        if user:
            auth_user = user
        else:
            user_model = get_user_model()
            auth_user = user_model.objects.all().first()
        return auth_user

    def validate(self, data):
        """
        Validates data
        :param data: Input data
        :return: Validated data
        :rtype: Object
        """
        model_type = self.model_type
        model_qs = ContentType.objects.filter(model=model_type)
        self.validation_error(model_qs, 'This is not a valid content type')
        any_model = model_qs.first().model_class()
        if self.slugify:
            obj_qs = any_model.objects.filter(slug=self.key)
            self.validation_error(obj_qs, 'This is not a slug for this content type')
        else:
            obj_qs = any_model.objects.filter(pk=self.key)
            self.validation_error(obj_qs, 'This is not a primary key for this content type')
        return data

    def validation_error(self, qs, error_msg):
        """
        Raises validation error
        :param obj_qs: Model or object queryset
        :param error_msg: Validation error message
        :return: None:
        :rtype: None
        """
        if not qs.exists() or qs.count() != 1:
            raise ValidationError(error_msg)