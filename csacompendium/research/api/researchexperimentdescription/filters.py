from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import ResearchExperimentDescription


class ResearchExperimentDescriptionListFilter(FilterSet):
    """
    Filter query list from research experiment description database table
    """
    class Meta:
        model = ResearchExperimentDescription
        fields = {'experimentdescription': ['exact'],
                  'object_id': ['exact'],
                  'content_type': ['exact'],
                  }
        order_by = ['experimentdescription']
