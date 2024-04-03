from django.urls import path 
from django.urls import path
from Pagination.views import AJIOListAPIView 

urlpatterns = [

    
    path('api/' ,AJIOListAPIView.as_view()),
    path('api/<int:pk>/' ,AJIOListAPIView.as_view()), 

]
