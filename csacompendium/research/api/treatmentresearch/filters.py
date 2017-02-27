
from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import TreatmentResearch


class TreatmentResearchListFilter(FilterSet):
    """
    Filter query list from treatment research database
    """
    class Meta:
        model = TreatmentResearch
        fields = {
            'experimentrep': ['exact'],
            'experimentdetails': ['exact'],
            'nitrogenapplied': ['exact'],
            'experimentduration': ['exact'],
            'object_id': ['exact'],
            'content_type': ['exact'],
        }
        order_by = ['experimentrep']
