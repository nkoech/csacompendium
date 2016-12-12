from django.conf.urls import url
from .views import (
    experiment_rep_views,
    nitrogen_applied_views,
    experiment_details_views,
    control_research_views,
    treatment_research_views,
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

# Experiment details URLs
urlpatterns += [
    url(
        r'^experimentdetails/$',
        experiment_details_views['ExperimentDetailsListAPIView'].as_view(),
        name='experiment_details_list'
    ),
    url(
        r'^experimentdetails/create/$',
        experiment_details_views['ExperimentDetailsCreateAPIView'].as_view(),
        name='experiment_details_create'
    ),
    url(
        r'^experimentdetails/(?P<slug>[\w-]+)/$',
        experiment_details_views['ExperimentDetailsDetailAPIView'].as_view(),
        name='experiment_details_detail'
    ),
]

# Control research URLs
urlpatterns += [
    url(
        r'^controlresearch/$',
        control_research_views['ControlResearchListAPIView'].as_view(),
        name='control_research_list'
    ),
    url(
        r'^controlresearch/create/$',
        control_research_views['ControlResearchCreateAPIView'].as_view(),
        name='control_research_create'
    ),
    url(
        r'controlresearch/(?P<pk>[\w-]+)/$',
        control_research_views['ControlResearchDetailAPIView'].as_view(),
        name='control_research_detail'
    ),
]

# Treatment research URLs
urlpatterns += [
    url(
        r'^treatmentresearch/$',
        treatment_research_views['TreatmentResearchListAPIView'].as_view(),
        name='treatment_research_list'
    ),
    url(
        r'^treatmentresearch/create/$',
        treatment_research_views['TreatmentResearchCreateAPIView'].as_view(),
        name='treatment_research_create'
    ),
    url(
        r'treatmentresearch/(?P<pk>[\w-]+)/$',
        treatment_research_views['TreatmentResearchDetailAPIView'].as_view(),
        name='treatment_research_detail'
    ),
]