from rest_framework.filters import (
    FilterSet
)
from csacompendium.research_type.models import ExperimentUnitCategory


class ExperimentUnitCategoryListFilter(FilterSet):
    """
    Filter query list from experiment unit category database table
    """
    class Meta:
        model = ExperimentUnitCategory
        fields = {
            'unit_category': ['iexact', 'icontains'],
        }
        order_by = ['unit_category']
