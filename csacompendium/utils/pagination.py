from rest_framework.pagination import LimitOffsetPagination


class CountryLimitOffsetPagination(LimitOffsetPagination):
    """
    Pagination class
    """
    default_limit = 2
    max_limit = 10