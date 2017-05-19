from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.keywordsearch import get_query, get_project_models
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListAPIView
from csacompendium.search.api.globalsearch.globalsearchserializers import global_search_serializers


def global_search_views():
    """
    Global search views
    :return: All global search views
    :rtype: Object
    """
    global_search_serializer = global_search_serializers()

    class GlobalSearchListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        serializer_class = global_search_serializer['GlobalSearchListSerializer']
        pagination_class = APILimitOffsetPagination

        def get_queryset(self):
            query_param = self.request.query_params.get('query', None)
            if query_param:
                global_results = []
                for model in get_project_models():
                    entry_query = get_query(query_param, model)
                    if entry_query:
                        query_result = model.objects.filter(entry_query)
                        global_results += query_result
                if global_results:
                    global_results.sort(key=lambda x: x.time_created)
                    return global_results
            return None

    return {
        'GlobalSearchListAPIView': GlobalSearchListAPIView
    }
