from Pagination.models import AJIO
from Pagination.serializers import AJIOSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination , LimitOffsetPagination
from .page import CustomPagination2
# from Pagination.page import Pagination

class AJIOListAPIView(ListAPIView): 

    queryset = AJIO.objects.all()
    serializer_class = AJIOSerializer 
    search_fields = ('vendor_id','vendor_name')
    # pagination_class = PageNumberPagination
    pagination_class = PageNumberPagination

