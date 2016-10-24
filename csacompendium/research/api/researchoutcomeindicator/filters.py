from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import ResearchOutcomeIndicator


class ResearchOutcomeListFilter(FilterSet):
    """
    Filter query list from research outcome indicator database table
    """
    class Meta:
        model = ResearchOutcomeIndicator
        fields = {'research': ['exact'],
                  'object_id': ['exact'],
                  'content_type': ['exact'],
                  }
        order_by = ['research']
