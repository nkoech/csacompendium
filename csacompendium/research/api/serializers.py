from .research.researchserializers import research_serializers
from .nitrogenapplied.nitrogenappliedserializers import nitrogen_applied_serializers
from .measurementyear.measurementyearserializers import measurement_year_serializers
from .researchdiversity.researchdiversityserializers import research_diversity_serializers
from .diversity.diversityserializers import diversity_serializers
from .researchexperimentdescription.researchexperimentdescriptionserializers import \
    research_experiment_description_serializers
from .experimentdescription.experimentdescriptionserializers import experiment_description_serializers
from .researchexperimentreplicate.researchexperimentreplicateserializers import \
    research_experiment_replicate_serializers
from .experimentreplicate.experimentreplicateserializers import experiment_replicate_serializers
from .researchauthor.researchauthorserializer import research_author_serializers
from .journal.journalserializers import journal_serializers
from .author.authorserializers import author_serializers
from .experimentunit.experimentunitserializers import experiment_unit_serializers
from .researchexperimentunit.researchexperimentunitserializers import research_experiment_unit_serializers
from .breed.breedserializers import breed_serializers
from .experimentunitcategory.experimentunitcategoryserializers import experiment_unit_category_serializers


research_serializers = research_serializers()
nitrogen_applied_serializers = nitrogen_applied_serializers()
measurement_year_serializers = measurement_year_serializers()
research_diversity_serializers = research_diversity_serializers()
diversity_serializers = diversity_serializers()
research_experiment_description_serializers = research_experiment_description_serializers()
experiment_description_serializers = experiment_description_serializers()
research_experiment_replicate_serializers = research_experiment_replicate_serializers()
experiment_replicate_serializers = experiment_replicate_serializers()
research_author_serializers = research_author_serializers()
journal_serializers = journal_serializers()
author_serializers = author_serializers()
experiment_unit_serializers = experiment_unit_serializers()
research_experiment_unit_serializers = research_experiment_unit_serializers()
breed_serializers = breed_serializers()
experiment_unit_category_serializers = experiment_unit_category_serializers()
