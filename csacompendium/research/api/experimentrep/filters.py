from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import ExperimentRep


class ExperimentRepListFilter(FilterSet):
    """
    Filter query list from experiment replication database table
    """
    class Meta:
        model = ExperimentRep
        fields = {
            'no_replication': ['exact', 'gte', 'lte'],
        }
        order_by = ['no_replication']
