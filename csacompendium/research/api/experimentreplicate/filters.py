from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import ExperimentReplicate


class ExperimentReplicateListFilter(FilterSet):
    """
    Filter query list from experiment replicate database table
    """
    class Meta:
        model = ExperimentReplicate
        fields = {
            'no_replicate': ['exact', 'gte', 'lte'],
        }
        order_by = ['no_replicate']
