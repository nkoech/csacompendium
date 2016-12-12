# from csacompendium.csa_practice.models import CsaPractice
from csacompendium.research_type.models import (
    ControlResearch,
    ExperimentRep,
    NitrogenApplied,
    ExperimentDetails,
)
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import (
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

    def create_control_research_serializer(model_type=None, unique_id=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param unique_id: A slug or primary key depending on what is passed
        :param user: Record owner
        :return: Serializer class
        :rtype: Object
        """

        class ControlResearchCreateSerializer(CreateSerializerUtil):
            """
            Create a record
            """

            class Meta:
                model = ControlResearch
                # fields = ['id', 'csapractice', 'experimentrep', 'experimentdetails',
                #           'nitrogenapplied', 'last_update', 'time_created', ]
                fields = ['id', 'experimentrep', 'experimentdetails',
                          'nitrogenapplied', 'last_update', 'time_created', ]

            def __init__(self, *args, **kwargs):
                super(ControlResearchCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = unique_id
                self.user = user
                if valid_integer(unique_id):
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
                # csapractice = validated_data.get('csapractice')
                experimentrep = validated_data.get('experimentrep')
                experimentdetails = validated_data.get('experimentdetails')
                nitrogenapplied = validated_data.get('nitrogenapplied')
                control_research = ControlResearch.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    # csapractice=csapractice,
                    experimentrep=experimentrep,
                    experimentdetails=experimentdetails,
                    nitrogenapplied=nitrogenapplied,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if control_research:
                    return control_research
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return ControlResearchCreateSerializer

    class ControlResearchListSerializer:
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_type_api:control_research_detail', 'pk')

        class Meta:
            model = ControlResearch
            fields = ['id', 'url', ]

    class ControlResearchDetailSerializer(FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        csa_practice_url = SerializerMethodField()
        experiment_replications_url = SerializerMethodField()
        experiment_details_url = SerializerMethodField()
        nitrogen_applied_url = SerializerMethodField()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        content_type_url = SerializerMethodField()

        class Meta:
            common_fields = [
                'modified_by',
                'last_update',
                'time_created',
                'content_type_url',
            ]
            model = ControlResearch
            fields = ['id', 'csa_practice_url', 'experiment_replications_url',
                      'experiment_details_url', 'nitrogen_applied_url', 'user'] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_csa_practice_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return None
            # return get_related_content_url(CsaPractice, obj.csapractice.id)

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

    return {
        'create_control_research_serializer': create_control_research_serializer,
        'ControlResearchListSerializer': ControlResearchListSerializer,
        'ControlResearchDetailSerializer': ControlResearchDetailSerializer
    }
