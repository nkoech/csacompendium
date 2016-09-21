from rest_framework.filters import (
    FilterSet
)
from csacompendium.soils.models import SoilType


class SoilTypeListFilter(FilterSet):
    """
    Filter query list from soil type database
    """
    class Meta:
        model = SoilType
        fields = {'soil_type': ['iexact', 'icontains'],
                  'classification': ['iexact', 'icontains'],
                  }
        order_by = ['soil_type']
