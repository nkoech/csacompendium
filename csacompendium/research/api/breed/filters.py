from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import Breed


class BreedListFilter(FilterSet):
    """
    Filter query list from breed database
    """
    class Meta:
        model = Breed
        fields = {
            'breed': ['iexact', 'icontains'],
            'object_id': ['exact'],
            'content_type': ['exact'],
        }
        order_by = ['breed']
