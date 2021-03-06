from .csapractice.csapracticeserializers import csa_practice_serializers
from .researchcsapractice.researchcsapracticeserializers import research_csa_practice_serializers
from .csatheme.csathemeserializers import csa_theme_serializers
from .practicelevel.practicelevelserializers import practice_level_serializers
from .practicetype.practicetypeserializers import practice_type_serializers

csa_practice_serializers = csa_practice_serializers()
research_csa_practice_serializers = research_csa_practice_serializers()
csa_theme_serializers = csa_theme_serializers()
practice_level_serializers = practice_level_serializers()
practice_type_serializers = practice_type_serializers()
