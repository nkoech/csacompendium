from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/country/', include('csacompendium.countries.api.urls', namespace='country_api'))
]
