from django.utils.text import slugify


def create_slug(instance, model=None, instance_field=None, new_slug=None):
    """
    Create a slug from country name.
    :param instance: Object instance
    :param model: Name of model
    :param instance_field: Field to be slugified
    :param new_slug: Newly created slug
    :return: Unique slug
    :rtype: string
    """
    slug = slugify(instance_field)
    if new_slug is not None:
        slug = new_slug
    qs = model.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '{0}-{1}'.format(slug, qs.first().id)
        return create_slug(instance, model, instance_field, new_slug=new_slug)
    return slug

