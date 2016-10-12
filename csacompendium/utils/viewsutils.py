from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin


class DetailViewUpdateDelete(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
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
