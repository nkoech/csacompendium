from django.conf.urls import url
from .views import (
    global_search_views,
)

# Outcome indicator URLs
urlpatterns = [
    url(
        r'^$',
        global_search_views['GlobalSearchListAPIView'].as_view(),
        name='global_search_list'
    ),
]
