from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import ResearchNitrogenApplied


class ResearchNitrogenAppliedListFilter(FilterSet):
    """
    Filter query list from research nitrogen applied database table
    """
    class Meta:
        model = ResearchNitrogenApplied
        fields = {'nitrogenapplied': ['exact'],
                  'object_id': ['exact'],
                  'content_type': ['exact'],
                  }
        order_by = ['nitrogenapplied']
