from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
# from csacompendium.research.api.research.researchserializers import research_serializers
from csacompendium.research.models import ExperimentDuration
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity


def experiment_duration_serializers():
    """
    Experiment duration serializers
    :return: All experiment duration  serializers
    :rtype: Object
    """

    class ExperimentDurationListSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:experiment_duration_detail', 'pk')

        class Meta:
            model = ExperimentDuration
            fields = [
                'exp_duration',
                'url',
            ]

    class ExperimentDurationDetailSerializer(ModelSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        # research_serializers = research_serializers()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        research = SerializerMethodField()

        class Meta:
            common_fields = [
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'research',
            ]
            model = ExperimentDuration
            fields = [
                'id',
                'exp_duration',
            ] + common_fields
            read_only_fields = ['id', ] + common_fields

        def get_user(self, obj):
            """
            :param obj: Current record object
            :return: Name of user who created the record
            :rtype: String
            """
            return str(obj.user.username)

        def get_modified_by(self, obj):
            """
            :param obj: Current record object
            :return: Name of user who edited a record
            :rtype: String
            """
            return str(obj.modified_by.username)

        def get_research(self, obj):
            """
            :param obj: Current record object
            :return: Research object
            :rtype: Object/record
            """
            request = self.context['request']
            # ResearchListSerializer = self.research_serializers['ResearchListSerializer']
            try:
                pass
                # research = ResearchListSerializer(
                #     obj.research_relation,
                #     context={'request': request},
                #     many=True
                # ).data
                # return research
            except obj.DoesNotExist:
                return None

    return {
        'ExperimentDurationListSerializer': ExperimentDurationListSerializer,
        'ExperimentDurationDetailSerializer': ExperimentDurationDetailSerializer
    }
