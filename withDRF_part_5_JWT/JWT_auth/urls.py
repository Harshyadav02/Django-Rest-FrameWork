from django.urls import path
# from rest_framework_jwtsimple.views import obtain_jwt_token , verify_jwt_token , refresh_jwt_token
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView , TokenVerifyView 
from JWT_auth.views import EmployeeListCreateAPIView ,EmployeeRetriveUpdateDeleteAPIView
# importing auth
from django.urls import path 

urlpatterns = [

    
    path('api/' ,EmployeeListCreateAPIView.as_view()),
    path('api/<int:pk>/' ,EmployeeRetriveUpdateDeleteAPIView.as_view()), 
    
    path('api-obtain-auth/', TokenObtainPairView.as_view()),
    path('api-refresh-auth/',TokenRefreshView.as_view()),
    path('api-verify-auth/', TokenVerifyView.as_view()),

]
