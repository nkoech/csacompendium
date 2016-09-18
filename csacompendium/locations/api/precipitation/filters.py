from rest_framework.filters import (
    FilterSet
)
from csacompendium.locations.models import Precipitation


class PrecipitationListFilter(FilterSet):
    """
    Filter query list from precipitation database
    """
    class Meta:
        model = Precipitation
        fields = {'precipitation_uom': ['iexact', 'icontains'],
                  'precipitation': ['exact', 'gte', 'lte'],
                  'precipitation_desc': ['icontains'],
                  }
        order_by = ['precipitation']
