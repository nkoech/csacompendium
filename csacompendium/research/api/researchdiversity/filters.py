from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import ResearchDiversity


class ResearchDiversityListFilter(FilterSet):
    """
    Filter query list from research diversity database table
    """
    class Meta:
        model = ResearchDiversity
        fields = {'diversity': ['exact'],
                  'object_id': ['exact'],
                  'content_type': ['exact'],
                  }
        order_by = ['diversity']
