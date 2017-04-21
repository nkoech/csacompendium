from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import MeasurementSeason


class MeasurementSeasonListFilter(FilterSet):
    """
    Filter query list from measurement season database table
    """
    class Meta:
        model = MeasurementSeason
        fields = {
            'measurement_season': ['iexact', 'icontains'],
        }
        order_by = ['measurement_season']
