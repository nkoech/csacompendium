from rest_framework.filters import (
    FilterSet
)
from csacompendium.locations.models import Temperature


class TemperatureListFilter(FilterSet):
    """
    Filter query list from temperature database
    """
    class Meta:
        model = Temperature
        fields = {'temperature_uom': ['iexact', 'icontains'],
                  'temperature': ['exact', 'gte', 'lte'],
                  }
        order_by = ['temperature']
