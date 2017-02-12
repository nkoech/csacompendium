from .treatmentresearch.treatmentresearchviews import treatment_research_views
from .controlresearch.controlresearchviews import control_research_views
from .experimentrep.experimentrepviews import experiment_rep_views
from .nitrogenapplied.nitrogenappliedviews import nitrogen_applied_views
from .experimentdetails.experimentdetailsviews import experiment_details_views
from .experimentduration.experimentdurationviews import experiment_duration_views
from .measurementyear.measurementyearviews import measurement_year_views
from .measurementseason.measurementseasonviews import measurement_season_views
from .researchauthor.researchauthorviews import research_author_views
from .author.authorviews import author_views


treatment_research_views = treatment_research_views()
control_research_views = control_research_views()
experiment_rep_views = experiment_rep_views()
nitrogen_applied_views = nitrogen_applied_views()
experiment_details_views = experiment_details_views()
experiment_duration_views = experiment_duration_views()
measurement_year_views = measurement_year_views()
measurement_season_views = measurement_season_views()
research_author_views = research_author_views()
author_views = author_views()
