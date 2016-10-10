from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import ObjectCategory


class ObjectCategoryListFilter(FilterSet):
    """
    Filter query list from object category database table
    """
    class Meta:
        model = ObjectCategory
        fields = {
            'object_category': ['iexact', 'icontains'],
        }
        order_by = ['object_category']
