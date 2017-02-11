
from rest_framework.filters import (
    FilterSet
)
from csacompendium.research_type.models import ControlResearch


class ControlResearchListFilter(FilterSet):
    """
    Filter query list from control research database
    """
    class Meta:
        model = ControlResearch
        fields = {
            'csapractice': ['exact'],
            'experimentrep': ['exact'],
            'experimentdetails': ['exact'],
            'nitrogenapplied': ['exact'],
            'experimentduration': ['exact'],
            'object_id': ['exact'],
            'content_type': ['exact'],
        }
        order_by = ['experimentrep']
