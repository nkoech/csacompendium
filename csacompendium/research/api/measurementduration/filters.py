from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import MeasurementDuration


class MeasurementDurationListFilter(FilterSet):
    """
    Filter query list from measurement duration database table
    """
    class Meta:
        model = MeasurementDuration
        fields = {
            'measurement_duration': ['exact', 'gte', 'lte'],
        }
        order_by = ['measurement_duration']
