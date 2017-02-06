from rest_framework.filters import (
    FilterSet
)
from csacompendium.indicators.models import IndicatorType


class IndicatorTypeListFilter(FilterSet):
    """
    Filter query list from indicator type database
    """
    class Meta:
        model = IndicatorType
        fields = {
            'indicator_type': ['iexact', 'icontains'],
        }
        order_by = ['indicator_type']
