from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import ResearchMeasurementYear


class ResearchMeasurementYearListFilter(FilterSet):
    """
    Filter query list from research measurement year database table
    """
    class Meta:
        model = ResearchMeasurementYear
        fields = {'measurementyear': ['exact'],
                  'object_id': ['exact'],
                  'content_type': ['exact'],
                  }
        order_by = ['measurementyear']
