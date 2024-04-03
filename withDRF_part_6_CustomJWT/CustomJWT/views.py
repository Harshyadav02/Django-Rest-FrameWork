from CustomJWT.models import AJIO
from rest_framework.permissions import IsAuthenticated
from CustomJWT.serializers import AJIOSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from CustomJWT.authenticate1 import  CustomAuthenticationBasedOnCondition

# TO implement token based authencation for Retive update and destory operations
class AJIOListCreateAPIView(ListCreateAPIView): 


    queryset = AJIO.objects.all()
    serializer_class = AJIOSerializer 
    # authentication_classes = [CustomAuthentication] 
    authentication_classes = [CustomAuthenticationBasedOnCondition]
    permission_classes = [IsAuthenticated]
   
# TO perform retrive update destroy in a single class 

class AJIORetriveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView) :

    queryset = AJIO.objects.all()
    serializer_class = AJIOSerializer


    

