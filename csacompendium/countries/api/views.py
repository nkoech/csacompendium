
from rest_framework.generics import ListAPIView
from csacompendium.countries.models import Country
from .serializers import CountrySerializer


class CountryListAPIView(ListAPIView):
    """
    Country API list view. To visualize all country records API.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
