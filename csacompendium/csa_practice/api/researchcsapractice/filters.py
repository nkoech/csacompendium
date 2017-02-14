from rest_framework.filters import (
    FilterSet
)
from csacompendium.csa_practice.models import ResearchCsaPractice


class ResearchCsaPracticeListFilter(FilterSet):
    """
    Filter query list from research CSA practice database table
    """
    class Meta:
        model = ResearchCsaPractice
        fields = {'csapractice': ['exact'],
                  'object_id': ['exact'],
                  'content_type': ['exact'],
                  }
        order_by = ['csapractice']
