from rest_framework.pagination import LimitOffsetPagination


class APILimitOffsetPagination(LimitOffsetPagination):
    """
    Pagination class
    """
    default_limit = 2
    max_limit = 10