from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import MeasurementYear


class MeasurementYearListFilter(FilterSet):
    """
    Filter query list from measurement year database
    """
    class Meta:
        model = MeasurementYear
        fields = {
            'meas_year': ['exact', 'gte', 'lte'],
        }
        order_by = ['meas_year']
