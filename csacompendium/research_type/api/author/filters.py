from rest_framework.filters import (
    FilterSet
)
from csacompendium.research_type.models import Author


class AuthorListFilter(FilterSet):
    """
    Filter query list from author database table
    """
    class Meta:
        model = Author
        fields = {'author_code': ['iexact', 'icontains'],
                  'first_name': ['iexact', 'icontains'],
                  'middle_name': ['iexact', 'icontains'],
                  'last_name': ['iexact', 'icontains'],
                  'author_bio': ['iexact', 'icontains'],
                  }
        order_by = ['last_name']
