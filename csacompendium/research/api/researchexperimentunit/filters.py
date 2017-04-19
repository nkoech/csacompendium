from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import ResearchExperimentUnit


class ResearchExperimentUnitListFilter(FilterSet):
    """
    Filter query list from research experiment unit database
    """
    class Meta:
        model = ResearchExperimentUnit
        fields = {
            'experimentunit': ['exact'],
            'breed': ['exact'],
            'object_id': ['exact'],
            'content_type': ['exact'],
        }
        order_by = ['breed']
