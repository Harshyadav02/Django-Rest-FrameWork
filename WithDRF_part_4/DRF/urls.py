from django.urls import path , include
from DRF.views import EmployeeListCreateAPIView ,EmployeeRetriveUpdateDeleteAPIView
# importing auth

from rest_framework.authtoken import views
urlpatterns = [

   

    path('api/' ,EmployeeListCreateAPIView.as_view()),
    path('api/<int:pk>/' ,EmployeeRetriveUpdateDeleteAPIView.as_view()),   


    # registration of url for authentication  here views is import from rest_framework and obtain_auth_token is function based view available in rest_framework.authtoken
    path('token/', views.obtain_auth_token ) 
]

