from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import Breed


class BreedListFilter(FilterSet):
    """
    Filter query list from breed database table
    """
    class Meta:
        model = Breed
        fields = {
            'breed': ['iexact', 'icontains'],
        }
        order_by = ['breed']
