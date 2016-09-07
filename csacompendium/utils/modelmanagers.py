from django.contrib.contenttypes.models import ContentType


def model_instance_filter(call_instance, current_instance, model_manager):
    """
    Query a related object/record from another model's object
    :param instance: Object instance
    :return: Query result from content type/model
    :rtye: object/record
    """
    content_type = ContentType.objects.get_for_model(call_instance.__class__)
    obj_id = call_instance.id
    qs = super(model_manager, current_instance).filter(content_type=content_type, object_id=obj_id)
    return qs