from rest_framework.filters import (
    FilterSet
)
from csacompendium.soils.models import Soil


class SoilListFilter(FilterSet):
    """
    Filter query list from country database
    """
    class Meta:
        model = Soil
        fields = {
            'som': ['exact', 'gte', 'lte'],
            'initial_soc': ['exact', 'gte', 'lte'],
            'soil_ph': ['exact', 'gte', 'lte'],
            'soil_years': ['exact', 'gte', 'lte'],
        }
        order_by = ['som']
