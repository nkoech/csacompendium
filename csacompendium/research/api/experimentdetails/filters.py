from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import ExperimentDetails


class ExperimentDetailsListFilter(FilterSet):
    """
    Filter query list from experiment details database table
    """
    class Meta:
        model = ExperimentDetails
        fields = {
            'exp_detail': ['iexact', 'icontains'],
        }
        order_by = ['exp_detail']

