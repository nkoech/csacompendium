
from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import ControlResearch


class ControlResearchListFilter(FilterSet):
    """
    Filter query list from control research database
    """
    class Meta:
        model = ControlResearch
        fields = {
            'experimentrep': ['exact'],
            'experimentdetails': ['exact'],
            'nitrogenapplied': ['exact'],
            'experimentduration': ['exact'],
            'object_id': ['exact'],
            'content_type': ['exact'],
        }
        order_by = ['experimentrep']
