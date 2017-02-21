from rest_framework.filters import (
    FilterSet
)
from csacompendium.research_type.models import ResearchExperimentUnit


class ResearchExperimentUnitListFilter(FilterSet):
    """
    Filter query list from research experiment unit database
    """
    class Meta:
        model = ResearchExperimentUnit
        fields = {
            'experimentunit': ['exact'],
            'upper_soil_depth': ['exact', 'gte', 'lte'],
            'lower_soil_depth': ['exact', 'gte', 'lte'],
            'incubation_days': ['exact', 'gte', 'lte'],
            'object_id': ['exact'],
            'content_type': ['exact'],
        }
        order_by = ['upper_soil_depth']
