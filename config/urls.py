from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/indicatoroutcome/', include('csacompendium.indicators.api.urls', namespace='indicator_outcome_api')),
    url(r'^api/csapractice/', include('csacompendium.csa_practice.api.urls', namespace='csa_practice_api')),
    url(r'^api/researchtype/', include('csacompendium.research_type.api.urls', namespace='research_type_api')),
    url(r'^api/research/', include('csacompendium.research.api.urls', namespace='research_api')),
    url(r'^api/soil/', include('csacompendium.soils.api.urls', namespace='soil_api')),
    url(r'^api/location/', include('csacompendium.locations.api.urls', namespace='location_api')),
    url(r'^api/country/', include('csacompendium.countries.api.urls', namespace='country_api'))
]
