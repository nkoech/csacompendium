from rest_framework.filters import (
    FilterSet
)
from csacompendium.indicators.models import ExperimentOutcome


class ExperimentOutcomeListFilter(FilterSet):
    """
    Filter query list from experiment outcome database table
    """
    class Meta:
        model = ExperimentOutcome
        fields = {
            'mean_outcome': ['exact', 'gte', 'lte'],
            'std_outcome': ['exact', 'gte', 'lte'],
            'outcome_uom': ['iexact', 'icontains'],
        }
        order_by = ['mean_outcome']
