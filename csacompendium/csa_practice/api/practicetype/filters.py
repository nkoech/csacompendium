from rest_framework.filters import (
    FilterSet
)
from csacompendium.csa_practice.models import PracticeType


class PracticeTypeListFilter(FilterSet):
    """
    Filter query list from practice type database
    """
    class Meta:
        model = PracticeType
        fields = {
            'practice_type': ['iexact', 'icontains'],
        }
        order_by = ['practice_type']
