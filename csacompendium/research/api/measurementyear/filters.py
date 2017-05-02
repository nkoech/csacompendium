from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import MeasurementYear


class MeasurementYearListFilter(FilterSet):
    """
    Filter query list from measurement year database table
    """
    class Meta:
        model = MeasurementYear
        fields = {
            'measurement_year': ['iexact', 'icontains'],
            'second_year': ['iexact', 'icontains'],
        }
        order_by = ['measurement_year']
