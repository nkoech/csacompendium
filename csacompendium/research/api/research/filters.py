
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
            'experimentrep': ['exact'],
            'experiment_description': ['iexact', 'icontains'],
            'nitrogenapplied': ['exact'],
            'measurementyear': ['exact'],
            'mean_outcome': ['exact'],
            'std_outcome': ['exact'],
            'outcome_uom': ['iexact', 'icontains'],
            'object_id': ['exact'],
            'content_type': ['exact'],
        }
        order_by = ['experiment_design']
