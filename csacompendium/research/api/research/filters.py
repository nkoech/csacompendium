
from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import Research


class ResearchListFilter(FilterSet):
    """
    Filter query list from research database
    """
    class Meta:
        model = Research
        fields = {
            'experiment_design': ['iexact', 'icontains'],
            'nitrogenapplied': ['exact'],
            'object_id': ['exact'],
            'content_type': ['exact'],
        }
        order_by = ['experiment_design']
