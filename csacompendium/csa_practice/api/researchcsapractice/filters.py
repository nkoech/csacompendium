from rest_framework.filters import (
    FilterSet
)
from csacompendium.indicators.models import ResearchOutcomeIndicator


class ResearchOutcomeIndicatorListFilter(FilterSet):
    """
    Filter query list from research outcome indicator database table
    """
    class Meta:
        model = ResearchOutcomeIndicator
        fields = {'outcomeindicator': ['exact'],
                  'object_id': ['exact'],
                  'content_type': ['exact'],
                  }
        order_by = ['outcomeindicator']