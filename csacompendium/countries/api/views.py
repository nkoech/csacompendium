
from rest_framework.generics import ListAPIView
from csacompendium.countries.models import Country


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
