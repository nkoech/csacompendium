from rest_framework.filters import (
    FilterSet
)
from csacompendium.research_type.models import ResearchAuthor


class ResearchAuthorListFilter(FilterSet):
    """
    Filter query list from research author database table
    """
    class Meta:
        model = ResearchAuthor
        fields = {'author': ['exact'],
                  'object_id': ['exact'],
                  'content_type': ['exact'],
                  }
        order_by = ['author']
