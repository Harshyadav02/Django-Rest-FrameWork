'''This file contains the configuration code of  custom pagination '''

'''DRF provides pagination in three ways 
    1) PageNumberPagination
    2) LimitOffSet
    3) CursorPagination
'''
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination, CursorPagination

# Creating own custom pagination class  for a particular view of we can just use PageNumberPagination in our view directly but we have created a custom pagination class for our understanding 
class Pagination(PageNumberPagination) :

    page_size = 5    # Total number of page size
    page_query_param = 'page'   # parameter for pagination 
    page_size_query_param = 'num' # parameter for query 
    max_page_size = 15  # Maxiumum size of entry on per page 

# Creating own custom pagination class  for a particular view by the help if LimitOffSet class 

class CustomPagination(LimitOffsetPagination) :

    # default value of limit is the number  
    
    default_limit = 15  # changing the limit to 15  defalut limit is defined in settings.py (global pagination settings)

class CustomPagination2(CursorPagination) :

    ordering = 'id'
    page_size = 5
    
    