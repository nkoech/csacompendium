
from rest_framework.generics import ListAPIView
from csacompendium.countries.models import Country
from .serializers import CountrySerializer


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
