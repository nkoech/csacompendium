from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Check if the object is owned by the current user
    """

    message = 'You must be the owner of this object'
    safe_methods_1 = ['GET', 'PUT', 'DELETE']
    safe_methods_2 = ['GET', 'OPTIONS', 'HEAD', 'DELETE']

    def has_permission(self, request, view):
        """
        Check if request method is permitted
        :param request: Client request
        :param view: Application view
        :return: True if the user request method is safe
                otherwise do not grant permission
        :rtype: Boolean
        """
        if request.method in self.safe_methods_1:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Check if request method has permission in raletion to safe
        methods and grant permission
        :param request: client request
        :param view: application view
        :param obj: application object - current record
        :return: Grant access to object if true otherwise return permission
                 denied message to user
        :rtype: object creator
        """
        if request.method in self.safe_methods_2:
            return True
        return obj.user == request.user
