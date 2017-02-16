from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import ResearchObject


class ResearchObjectListFilter(FilterSet):
    """
    Filter query list from research object database
    """
    class Meta:
        model = ResearchObject
        fields = {
            'experimentobject': ['exact'],
            'upper_soil_depth': ['exact', 'gte', 'lte'],
            'lower_soil_depth': ['exact', 'gte', 'lte'],
            'object_id': ['exact'],
            'content_type': ['exact'],
        }
        order_by = ['upper_soil_depth']
