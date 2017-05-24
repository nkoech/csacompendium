from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^api/search/', include('csacompendium.search.api.urls', namespace='search')),
    url(r'^api/indicatoroutcome/', include('csacompendium.indicators.api.urls', namespace='indicator_outcome_api')),
    url(r'^api/csapractice/', include('csacompendium.csa_practice.api.urls', namespace='csa_practice_api')),
    url(r'^api/research/', include('csacompendium.research.api.urls', namespace='research_api')),
    url(r'^api/soil/', include('csacompendium.soils.api.urls', namespace='soil_api')),
    url(r'^api/location/', include('csacompendium.locations.api.urls', namespace='location_api')),
    url(r'^api/country/', include('csacompendium.countries.api.urls', namespace='country_api'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
