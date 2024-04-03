from django.urls import path , include
from DRF.views import EmployeeListAPIView,EmployeeCreateAPIView ,EmployeeRetriveAPIView ,EmployeeUpdateAPIView,EmployeeDestroyAPIView,EmployeeListCreateAPIView, EmployeeRetrieveUpdateAPIView,EmployeeRetriveDeleteAPIView,EmployeeRetriveUpdateDeleteAPIView


# importing auth

from rest_framework.authtoken import views
urlpatterns = [

    # path('api/' , EmployeeListAPIView.as_view()),
    # path('createapi/' , EmployeeCreateAPIView.as_view()),

    # # note pk is mandtory in it we can not take any other keyword like id etc.
    # path('retriveapi/<int:pk>' ,EmployeeRetriveAPIView.as_view()),

    # path('updateapi/<int:pk>' , EmployeeUpdateAPIView.as_view()),
    # path('destroyapi/<int:pk>' , EmployeeDestroyAPIView.as_view()),

    path('api/' ,EmployeeListCreateAPIView.as_view()),

    # path('retrieveupdate/<int:pk>' ,EmployeeRetrieveUpdateAPIView.as_view()),

    # path('retrievedelete/<int:pk>' ,EmployeeRetriveDeleteAPIView.as_view()),

    path('api/<int:pk>/' ,EmployeeRetriveUpdateDeleteAPIView.as_view()),   


    # registration of url for authentication  here views is import from rest_framework and obtain_auth_token is function based view available in rest_framework.authtoken
    path('token/', views.obtain_auth_token ) 
]




#  To retrive your token use

#http POST http://127.0.0.1:8000/<your configured api>/ username=<username> password=<password>  
