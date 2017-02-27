from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import NitrogenApplied


class NitrogenAppliedListFilter(FilterSet):
    """
    Filter query list from nitrogen applied database table
    """
    class Meta:
        model = NitrogenApplied
        fields = {
            'nitrogen_amount': ['exact', 'gte', 'lte'],
            'amount_uom': ['iexact', 'icontains'],
        }
        order_by = ['nitrogen_amount']
