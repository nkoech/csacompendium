from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import Diversity


class DiversityListFilter(FilterSet):
    """
    Filter query list from diversity database table
    """
    class Meta:
        model = Diversity
        fields = {
            'diversity': ['iexact', 'icontains'],
        }
        order_by = ['diversity']
