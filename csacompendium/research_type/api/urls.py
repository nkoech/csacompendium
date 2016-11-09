from django.conf.urls import url
from .views import (
    experiment_rep_views,
    nitrogen_applied_views,
)

# Experiment replication URLs
urlpatterns = [
    url(
        r'^experimentreplication/$',
        experiment_rep_views['ExperimentRepListAPIView'].as_view(),
        name='experiment_rep_list'
    ),
    url(
        r'^experimentreplication/create/$',
        experiment_rep_views['ExperimentRepCreateAPIView'].as_view(),
        name='experiment_rep_create'
    ),
    url(
        r'^experimentreplication/(?P<pk>[\w-]+)/$',
        experiment_rep_views['ExperimentRepDetailAPIView'].as_view(),
        name='experiment_rep_detail'
    ),
]

# Nitrogen Applied URLs
urlpatterns += [
    url(
        r'^nitrogenapplied/$',
        nitrogen_applied_views['NitrogenAppliedListAPIView'].as_view(),
        name='nitrogen_applied_list'
    ),
    url(
        r'^nitrogenapplied/create/$',
        nitrogen_applied_views['NitrogenAppliedCreateAPIView'].as_view(),
        name='nitrogen_applied_create'
    ),
    url(
        r'^nitrogenapplied/(?P<pk>[\w-]+)/$',
        nitrogen_applied_views['NitrogenAppliedDetailAPIView'].as_view(),
        name='nitrogen_applied_detail'
    ),
]
