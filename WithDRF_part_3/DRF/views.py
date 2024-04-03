from django.shortcuts import render
from rest_framework.views import APIView
from DRF.models import Employee
from DRF.serializers import EmployeeSerializer
from django.http import HttpResponse 
from rest_framework.response import Response


# We can make more easy to read operation by inheriting ListAPIView class we no no need to define get methods and all here is an example

'''class EmployeeListAPIView(APIView) :

    def get(self , request): 

       # getting all the employee details
       qs = Employee.objects.all() 

       # conveting the employee object to py dict
       serializer = EmployeeSerializer(qs , many = True)


       # returning json response Response convert p-dict to json automatically
       return Response(serializer.data)     # serializer.data is py-dict
'''

# Just an simple example for ListAPIView class
from rest_framework.generics import ListAPIView
class EmployeeListAPIView(ListAPIView) :
    # queryset and serializer_class are pre defined word in ListAPIView 

    # we have to gain all employee data and have to define serializer_class we no need to explacitly convert py dict to json and all stuff
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#  Like ListAPIView list all the employees there is a class to create(POST) employee named CreateAPIView 

from rest_framework.generics import CreateAPIView
class EmployeeCreateAPIView(CreateAPIView) : 

    # for which model you have to make post operation  retrive all the object form it 
    queryset = Employee.objects.all()

    # which is your serailizer class
    serializer_class = EmployeeSerializer


# performing retrive opertion based on pk
from rest_framework.generics import RetrieveAPIView 

class EmployeeRetriveAPIView(RetrieveAPIView): 

    # all the things are same just we have to change urls for this view
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# Update operation
    
from rest_framework.generics import UpdateAPIView
class EmployeeUpdateAPIView(UpdateAPIView) :

    # All the things will be same just we have to change urls for this update
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

from rest_framework.generics import DestroyAPIView
class EmployeeDestroyAPIView(DestroyAPIView) :

    # All the things will be same just we have to change urls for this delete
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



# We know that get and post donot talk about any pk since we have used ListAPIView and CreateAPIView from listing and creating data. Here is an commbined Class for doing the same thing named ListCreateAPIView both the work will be done by the same class
    



# To implement Retrive and destroy operations in a single class 
from rest_framework.generics import RetrieveDestroyAPIView
class EmployeeRetriveDeleteAPIView(RetrieveDestroyAPIView) :

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



# To perform Both retrive and update operations in single time we have to use RetriveUpdateAPIView 

from rest_framework.generics import RetrieveUpdateAPIView
class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView)     :

    queryset =Employee.objects.all()
    serializer_class = EmployeeSerializer


from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import TokenAuthentication      # TO implement token based authencation for Retive update and destory operations

from rest_framework.permissions import IsAuthenticated  , IsAdminUser ,IsAuthenticatedOrReadOnly
# we have imported type of authentication permissions
class EmployeeListCreateAPIView(ListCreateAPIView): 


    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer 
    # authentication_classes =  [TokenAuthentication]    # authentication_classes is inbuild varaible we have to specify whic type of authencation we are using so TokenAuthentication (imported from restframework)

    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    '''Note when you make request by  http http://127.0.0.1:8000/listcreate/ 
    #you will see some extra information like Content-type i.e application/json  
    and
    Allow:  this define which type of task your api  can do such as get post
    '''


# TO perform retrive update destroy in a single class 
from rest_framework.generics import RetrieveUpdateDestroyAPIView



# If user is an admin then only below opertion will be performed  
from rest_framework.permissions import IsAdminUser , IsAuthenticatedOrReadOnly

class EmployeeRetriveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView) :

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # authentication_classes = [TokenAuthentication]
    
    '''permission_classes = [IsAdminUser,]   # Here we have added IsAdmin if the user is admiin then only he able to Retive update and delete a user if some one tries to perform such action an error will occur saying {"detail":"You do not have permission to perform this action."} '''

    # permission_classes = [IsAuthenticatedOrReadOnly]

    #IsAuthenticatedOrReadOnly is best prmission for those type where get is allowed to any user but POST , PUT and patch is alllowed to specfic user 




'''
authentication_classes = [TokenAuthentication]    and permission_classes = [IsAuthenticated]   we have define these in every class but there is a way to overcome from it instead of defining them in each class add them at settings.py i.e adding them globally(check settings.py for more info)


suppose we have 10 api in which 8 have should have token and 2 of them donot need token to get the data once we have added the creadentails to our settings.py file the token authorazation will be for our 10 api now we can do that in the 2 api we donot need token we have to give permission = [AllowAny] inside the class locally 
'''