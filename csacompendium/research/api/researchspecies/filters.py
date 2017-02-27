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
        fields = {'species': ['exact'],
                  'object_id': ['exact'],
                  'content_type': ['exact'],
                  }
        order_by = ['species']
