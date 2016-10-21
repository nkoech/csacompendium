from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import ResearchSpecies


class ResearchSpeciesListFilter(FilterSet):
    """
    Filter query list from research species database table
    """
    class Meta:
        model = ResearchSpecies
        fields = {'research': ['exact'],
                  'object_id': ['exact'],
                  'content_type': ['exact'],
                  }
        order_by = ['research']
