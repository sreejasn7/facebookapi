__author__ = ""
__copyright__ = ""
__maintainer__ = ""
__version__ = ""

from rest_framework.pagination import PageNumberPagination


class LargeUserSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
