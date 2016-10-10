# from .soil.soilserializers import soil_serializers
from .measurementyear.measurementyearserializers import measurement_year_serializers
from .measurementseason.measurementseasonserializers import measurement_season_serializers
from .experimentduration.experimentdurationserializers import experiment_duration_serializers
from .objectcategory.objectcategoryserializers import object_category_serializers

# soil_serializers = soil_serializers()
measurement_year_serializers = measurement_year_serializers()
measurement_season_serializers = measurement_season_serializers()
experiment_duration_serializers = experiment_duration_serializers()
object_category_serializers = object_category_serializers()
