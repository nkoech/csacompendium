from rest_framework.filters import (
    FilterSet
)
from csacompendium.indicators.models import OutcomeIndicator


class OutcomeIndicatorListFilter(FilterSet):
    """
    Filter query list from outcome indicator database
    """
    class Meta:
        model = OutcomeIndicator
        fields = {'indicator_code': ['iexact', 'icontains'],
                  'indicator': ['exact'],
                  'subindicator': ['iexact', 'icontains'],
                  'definition': ['iexact', 'icontains'],
                  'common_uom': ['iexact', 'icontains'],
                  'indicatortype': ['exact'],
                  }
        order_by = ['indicator_code']

