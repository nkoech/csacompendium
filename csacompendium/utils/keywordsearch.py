import re
from django.db.models import Q


def get_query(query_string, obj=None, ):
    """
    Complex keyword queries using Django Q objects
    :param query_string: Keyword string to be searched
    :param obj: Object that could either be a model or a dictionary fields and lookup expressions
    :return: Object query based on keyword string otherwise return None 
    """
    query = None
    terms = _normalize_keyword(query_string)
    if not isinstance(obj, dict):
        obj = _get_search_fields(obj)
    if obj and terms:
        for term in terms:
            or_query = None  # Query to search for a given term in each field
            for k, v in obj.items():
                q = Q(**{"{0}__{1}".format(k, v): term})
                if or_query is None:
                    or_query = q
                else:
                    or_query = or_query | q
            if query is None:
                query = or_query
            else:
                query = query & or_query
        return query
    else:
        return None


def _get_search_fields(model):
    """
    Get search fields from a model
    :param model: Model object
    :return: Return a dictionary of fields together with lookup expressions otherwise return None
    """
    search_fields = {}
    field_types = ['Slugfield', 'Foreignkey']
    str_field_types = ['Charfield', 'Textfield']
    fields_names = ['object_id', 'content_object', 'time_created', 'last_update', 'id']
    try:
        if model:
            for field in model._meta.get_fields():
                verbose_name = getattr(field, 'verbose_name', None)
                if verbose_name:
                    field_name = str(field.name)
                    field_type = str(field.get_internal_type().title())
                    if field_name not in fields_names and field_type not in field_types:
                        if field_type in str_field_types:
                            search_fields[field_name] = 'icontains'
                        else:
                            search_fields[field_name] = 'exact'
            return search_fields
    except AssertionError:
        return None


def _normalize_keyword(
        query_string,
        findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
        normspace=re.compile(r'\s{2,}').sub
):
    """
    Breaks the string into a list based on spaces and double quotes
    :param query_string: String to be normalized
    :param findterms: Return all non-overlapping matches of regex pattern in string, as a list of strings
    :param normspace: Return the string obtained by replacing the leftmost non-overlapping occurrences of 
                      regex pattern in string by replacement
    :return: Normalized keywords in a list
    """
    return [normspace('', (t[0] or t[1]).strip()) for t in findterms(query_string)]