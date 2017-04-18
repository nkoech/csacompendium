from .research.researchviews import research_views
from .experimentrep.experimentrepviews import experiment_rep_views
from .nitrogenapplied.nitrogenappliedviews import nitrogen_applied_views
from .experimentduration.experimentdurationviews import experiment_duration_views
from .measurementyear.measurementyearviews import measurement_year_views
from .measurementseason.measurementseasonviews import measurement_season_views
from .researchauthor.researchauthorviews import research_author_views
from .journal.journalviews import journal_views
from .author.authorviews import author_views
from .experimentunit.experimentunitviews import experiment_unit_views
from .researchexperimentunit.researchexperimentunitviews import research_experiment_unit_views
from .breed.breedviews import breed_views
from .experimentunitcategory.experimentunitcategoryviews import experiment_unit_category_views


research_views = research_views()
experiment_rep_views = experiment_rep_views()
nitrogen_applied_views = nitrogen_applied_views()
experiment_duration_views = experiment_duration_views()
measurement_year_views = measurement_year_views()
measurement_season_views = measurement_season_views()
research_author_views = research_author_views()
journal_views = journal_views()
author_views = author_views()
experiment_unit_views = experiment_unit_views()
research_experiment_unit_views = research_experiment_unit_views()
breed_views = breed_views()
experiment_unit_category_views = experiment_unit_category_views()
