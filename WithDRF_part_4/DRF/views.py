from DRF.models import Employee

from DRF.serializers import EmployeeSerializer
from DRF.permissions import IsReadOnly,IsGETOrPATCH , SunnyPermisssion
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView
# TO implement token based authencation for Retive update and destory operations
class EmployeeListCreateAPIView(ListCreateAPIView): 


    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer 
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsReadOnly,]
    permission_classes = [SunnyPermisssion,]
# TO perform retrive update destroy in a single class 
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class EmployeeRetriveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView) :

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [SunnyPermisssion,]

    



