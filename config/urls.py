from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/soil/', include('csacompendium.research.api.urls', namespace='research_api')),
    url(r'^api/soil/', include('csacompendium.soils.api.urls', namespace='soil_api')),
    url(r'^api/location/', include('csacompendium.locations.api.urls', namespace='location_api')),
    url(r'^api/country/', include('csacompendium.countries.api.urls', namespace='country_api'))
]
