from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin


class DetailViewUpdateDelete(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    """
    Updates and deletes records in the view detail serializer
    """
    def put(self, request, *args, **kwargs):
        """
        Update record
        :param request: Client request
        :param args: List arguments
        :param kwargs: Keyworded arguments
        :return: Updated record
        :rtype: Object
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Delete record
        :param request: Client request
        :param args: List arguments
        :param kwargs: Keyworded arguments
        :return: Updated record
        :rtype: Object
        """
        return self.destroy(request, *args, **kwargs)

    def perform_update(self, serializer):
        """
        Update a field
        :param serializer: Serializer object
        :return:
        """
        serializer.save(modified_by=self.request.user)


def get_http_request(request, slug=False):
    """
    Get http request values
    :param request:
    :param slug: Checks if slug is provided
    :return: Content/model type, request parameter and user creator
    :rtype: String
    """

    model_type = request.GET.get('type')
    url_parameter = request.GET.get('pk')
    user = request.user
    if slug:
        url_parameter = request.GET.get('slug')
    return model_type, url_parameter, user
