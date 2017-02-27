from csacompendium.research.models import (
    ControlResearch,
    ExperimentRep,
    NitrogenApplied,
    ExperimentDetails,
    ExperimentDuration,
    MeasurementYear,
)
from csacompendium.research.api.researchauthor.researchauthorserializer import research_author_serializers
from csacompendium.research.api.researchspecies.researchspeciesserializers import research_species_serializers
from csacompendium.indicators.api.researchoutcomeindicator.researchoutcomeindicatorserializers import \
    research_outcome_indicator_serializers
from csacompendium.csa_practice.api.researchcsapractice.researchcsapracticeserializers import \
    research_csa_practice_serializers
from csacompendium.research.api.researchexperimentunit.researchexperimentunitserializers import \
    research_experiment_unit_serializers
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import (
    get_related_content,
    get_related_content_url,
    valid_integer,
    CreateSerializerUtil,
    FieldMethodSerializer,
)
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)


def control_research_serializers():
    """
    Control research serializers
    :return: All control research serializers
    :rtype: Object
    """

    def create_control_research_serializer(model_type=None, request_key=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param request_key: A slug or primary key depending on what is passed
        :param user: Record owner
        :return: Serializer class
        :rtype: Object
        """

        class ControlResearchCreateSerializer(ModelSerializer, CreateSerializerUtil):
            """
            Create a record
            """
            class Meta:
                model = ControlResearch
                fields = ['id', 'experimentrep', 'experimentdetails', 'nitrogenapplied',
                          'experimentduration', 'measurementyear', 'mean_outcome',
                          'std_outcome', 'outcome_uom', 'last_update', 'time_created', ]

            def __init__(self, *args, **kwargs):
                super(ControlResearchCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = request_key
                self.user = user
                if valid_integer(request_key):
                    self.slugify = False
                else:
                    self.slugify = True
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Control research object
                :rtype: Object
                """
                experimentrep = validated_data.get('experimentrep')
                experimentdetails = validated_data.get('experimentdetails')
                nitrogenapplied = validated_data.get('nitrogenapplied')
                experimentduration = validated_data.get('experimentduration')
                measurementyear = validated_data.get('measurementyear')
                mean_outcome = validated_data.get('mean_outcome')
                std_outcome = validated_data.get('std_outcome')
                outcome_uom = validated_data.get('outcome_uom')

                control_research = ControlResearch.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    experimentrep=experimentrep,
                    experimentdetails=experimentdetails,
                    nitrogenapplied=nitrogenapplied,
                    experimentduration=experimentduration,
                    measurementyear=measurementyear,
                    mean_outcome=mean_outcome,
                    std_outcome=std_outcome,
                    outcome_uom=outcome_uom,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if control_research:
                    return control_research
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return ControlResearchCreateSerializer

    class ControlResearchListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:control_research_detail', 'pk')

        class Meta:
            model = ControlResearch
            fields = ['id', 'mean_outcome', 'std_outcome', 'outcome_uom', 'url', ]

    class ControlResearchDetailSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        experiment_replications_url = SerializerMethodField()
        experiment_details_url = SerializerMethodField()
        nitrogen_applied_url = SerializerMethodField()
        experiment_duration_url = SerializerMethodField()
        measurement_year_url = SerializerMethodField()
        research_author_serializers = research_author_serializers()
        research_species_serializers = research_species_serializers()
        research_outcome_indicator_serializers = research_outcome_indicator_serializers()
        research_csa_practice_serializers = research_csa_practice_serializers()
        research_experiment_unit_serializers = research_experiment_unit_serializers()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        content_type_url = SerializerMethodField()
        authors = SerializerMethodField()
        species = SerializerMethodField()
        outcome_indicator = SerializerMethodField()
        csa_practice = SerializerMethodField()
        experiment_unit = SerializerMethodField()

        class Meta:
            common_fields = [
                'modified_by',
                'last_update',
                'time_created',
                'content_type_url',
                'authors',
                'species',
                'outcome_indicator',
                'csa_practice',
                'experiment_unit',
            ]
            model = ControlResearch
            fields = [
                'id', 'experiment_replications_url', 'experiment_details_url', 'nitrogen_applied_url',
                'experiment_duration_url', 'measurement_year_url', 'mean_outcome', 'std_outcome',
                'outcome_uom', 'user',
            ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_experiment_details_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(ExperimentRep, obj.experimentrep.id)

        def get_experiment_replications_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(ExperimentDetails, obj.experimentdetails.id)

        def get_nitrogen_applied_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(NitrogenApplied, obj.nitrogenapplied.id)

        def get_experiment_duration_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(ExperimentDuration, obj.experimentduration.id)

        def get_measurement_year_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(MeasurementYear, obj.measurementyear.id)

        def get_authors(self, obj):
            """
            :param obj: Current record object
            :return: Related author details
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchAuthorSerializer = self.research_author_serializers['ResearchAuthorSerializer']
            related_content = get_related_content(obj, ResearchAuthorSerializer, obj.research_author, request)
            return related_content

        def get_species(self, obj):
            """
            :param obj: Current record object
            :return: Related species details
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchSpeciesSerializer = self.research_species_serializers['ResearchSpeciesSerializer']
            related_content = get_related_content(obj, ResearchSpeciesSerializer, obj.research_species, request)
            return related_content

        def get_outcome_indicator(self, obj):
            """
            :param obj: Current record object
            :return: Related outcome indicator details
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchOutcomeIndicatorSerializer = self.research_outcome_indicator_serializers[
                'ResearchOutcomeIndicatorSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchOutcomeIndicatorSerializer, obj.research_outcome_indicator, request
            )
            return related_content

        def get_csa_practice(self, obj):
            """
            :param obj: Current record object
            :return: Related CSA practice details
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchCsaPracticeSerializer = self.research_csa_practice_serializers[
                'ResearchCsaPracticeSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchCsaPracticeSerializer, obj.research_csa_practice, request
            )
            return related_content

        def get_experiment_unit(self, obj):
            """
            :param obj: Current record object
            :return: Related experiment unit details
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchExperimentUnitSerializer = self.research_experiment_unit_serializers[
                'ResearchExperimentUnitSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchExperimentUnitSerializer, obj.research_experiment_unit, request
            )
            return related_content

    return {
        'create_control_research_serializer': create_control_research_serializer,
        'ControlResearchListSerializer': ControlResearchListSerializer,
        'ControlResearchDetailSerializer': ControlResearchDetailSerializer
    }
