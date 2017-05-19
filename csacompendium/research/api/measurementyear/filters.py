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
            'measurement_year': ['exact', 'gte', 'lte'],
            'second_year': ['exact', 'gte', 'lte'],
        }
        order_by = ['measurement_year']
