from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import ExperimentDuration


class ExperimentDurationListFilter(FilterSet):
    """
    Filter query list from experiment duration database table
    """
    class Meta:
        model = ExperimentDuration
        fields = {
            'exp_duration': ['exact', 'gte', 'lte'],
        }
        order_by = ['exp_duration']
