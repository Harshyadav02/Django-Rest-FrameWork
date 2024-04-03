from JWT_auth.models import Employee
from rest_framework.permissions import IsAuthenticated
from JWT_auth.serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

# TO implement token based authencation for Retive update and destory operations
class EmployeeListCreateAPIView(ListCreateAPIView): 


    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [SunnyPermisssion,]
# TO perform retrive update destroy in a single class 
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class EmployeeRetriveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView) :

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    


