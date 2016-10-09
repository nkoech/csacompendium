from rest_framework.filters import (
    FilterSet
)
from csacompendium.soils.models import Soil


class SoilListFilter(FilterSet):
    """
    Filter query list from soil database
    """
    class Meta:
        model = Soil
        fields = {
            'soiltype': ['exact'],
            'soiltexture': ['exact'],
            'som': ['exact', 'gte', 'lte'],
            'initial_soc': ['exact', 'gte', 'lte'],
            'soil_ph': ['exact', 'gte', 'lte'],
            'soil_years': ['exact', 'gte', 'lte'],
            'object_id': ['exact'],
            'content_type': ['exact'],
        }
        order_by = ['som']
