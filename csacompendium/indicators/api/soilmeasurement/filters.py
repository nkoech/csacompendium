from rest_framework.filters import (
    FilterSet
)
from csacompendium.indicators.models import SoilMeasurement


class SoilMeasurementListFilter(FilterSet):
    """
    Filter query list from soil measurement database table
    """
    class Meta:
        model = SoilMeasurement
        fields = {
            'upper_soil_depth': ['exact', 'gte', 'lte'],
            'lower_soil_depth': ['exact', 'gte', 'lte'],
            'depth_uom': ['iexact', 'icontains'],
            'incubation_days': ['exact', 'gte', 'lte'],
        }
        order_by = ['upper_soil_depth', 'lower_soil_depth']
