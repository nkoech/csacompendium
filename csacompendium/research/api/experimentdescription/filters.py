from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import ExperimentDescription


class ExperimentDescriptionListFilter(FilterSet):
    """
    Filter query list from experiment description database table
    """
    class Meta:
        model = ExperimentDescription
        fields = {
            'experiment_description': ['iexact', 'icontains'],
        }
        order_by = ['experiment_description']
