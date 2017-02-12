from rest_framework.filters import (
    FilterSet
)
from csacompendium.research_type.models import MeasurementYear


class MeasurementYearListFilter(FilterSet):
    """
    Filter query list from measurement year database table
    """
    class Meta:
        model = MeasurementYear
        fields = {
            'meas_year': ['exact', 'gte', 'lte'],
            'measurementseason': ['exact'],
        }
        order_by = ['meas_year']
