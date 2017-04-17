from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import Journal


class JournalListFilter(FilterSet):
    """
    Filter query list from journal database table
    """
    class Meta:
        model = Journal
        fields = {
            'journal_tag': ['iexact', 'icontains'],
            'publication_year': ['exact', 'gte', 'lte'],
        }
        order_by = ['publication_year']
