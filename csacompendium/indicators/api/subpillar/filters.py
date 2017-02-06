from rest_framework.filters import (
    FilterSet
)
from csacompendium.indicators.models import Subpillar


class SubpillarListFilter(FilterSet):
    """
    Filter query list from suboillar database table
    """
    class Meta:
        model = Subpillar
        fields = {'subpillar': ['iexact', 'icontains'], }
        order_by = ['subpillar']
