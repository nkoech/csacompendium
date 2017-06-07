
from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import Research

# Test for ContentType filter. To be used if need be
# from csacompendium.csa_practice.models import ResearchCsaPractice
# from django.contrib.contenttypes.models import ContentType
# import django_filters


class ResearchListFilter(FilterSet):
    """
    Filter query list from research database
    """

    # Test for ContentType filter. To be used if need be by adding to Meta fields
    # def _csa_practice_filter(qs, value):
    #     research = Research.objects.all()
    #     research_ctype = ContentType.objects.get_for_model(Research)
    #     if value:
    #         try:
    #             research_csa_practice = ResearchCsaPractice.objects.filter(
    #                 content_type=research_ctype,
    #                 object_id__in=[i.id for i in research]
    #             ).filter(csapractice__practice_code=value)
    #         except ResearchCsaPractice.DoesNotExist:
    #             return None
    #         return qs.filter(id__in=[i.id for i in research_csa_practice])
    #     return qs
    # csa_practice = django_filters.CharFilter(action=_csa_practice_filter)

    class Meta:
        model = Research
        fields = {
            'id': ['exact'],
            'research_code': ['iexact', 'icontains'],
            'experiment_design': ['iexact', 'icontains'],
            'object_id': ['exact'],
            'content_type': ['exact'],
        }
        order_by = ['id', 'research_code']
