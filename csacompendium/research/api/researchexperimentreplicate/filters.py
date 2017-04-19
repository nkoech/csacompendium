from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import ResearchExperimentReplicate


class ResearchExperimentReplicateListFilter(FilterSet):
    """
    Filter query list from research experiment replicate database table
    """
    class Meta:
        model = ResearchExperimentReplicate
        fields = {'experimentreplicate': ['exact'],
                  'object_id': ['exact'],
                  'content_type': ['exact'],
                  }
        order_by = ['experimentreplicate']
