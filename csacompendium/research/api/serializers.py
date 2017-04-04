from .research.researchserializers import research_serializers
from .experimentrep.experimentrepserializers import experiment_rep_serializers
from .nitrogenapplied.nitrogenappliedserializers import nitrogen_applied_serializers
from .experimentduration.experimentdurationserializers import experiment_duration_serializers
from .measurementyear.measurementyearserializers import measurement_year_serializers
from .measurementseason.measurementseasonserializers import measurement_season_serializers
from .researchauthor.researchauthorserializer import research_author_serializers
from .author.authorserializers import author_serializers
from .researchspecies.researchspeciesserializers import research_species_serializers
from .species.speciesserializers import species_serializers
from .experimentunit.experimentunitserializers import experiment_unit_serializers
from .researchexperimentunit.researchexperimentunitserializers import research_experiment_unit_serializers
from .experimentunitcategory.experimentunitcategoryserializers import experiment_unit_category_serializers
from .breed.breedserializers import breed_serializers


research_serializers = research_serializers()
experiment_rep_serializers = experiment_rep_serializers()
nitrogen_applied_serializers = nitrogen_applied_serializers()
experiment_duration_serializers = experiment_duration_serializers()
measurement_year_serializers = measurement_year_serializers()
measurement_season_serializers = measurement_season_serializers()
research_author_serializers = research_author_serializers()
author_serializers = author_serializers()
research_species_serializers = research_species_serializers()
species_serializers = species_serializers()
experiment_unit_serializers = experiment_unit_serializers()
research_experiment_unit_serializers = research_experiment_unit_serializers()
experiment_unit_category_serializers = experiment_unit_category_serializers()
breed_serializers = breed_serializers()
