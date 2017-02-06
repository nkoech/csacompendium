from rest_framework.filters import (
    FilterSet
)
from csacompendium.indicators.models import Indicator


class IndicatorListFilter(FilterSet):
    """
    Filter query list from indicator database
    """
    class Meta:
        model = Indicator
        fields = {'indicator': ['iexact', 'icontains'],
                  'subpillar': ['exact'],
                  }
        order_by = ['indicator']

