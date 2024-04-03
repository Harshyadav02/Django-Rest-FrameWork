from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from DRF.serializer import NameSerializer
from rest_framework.viewsets import ViewSet

# Note in APIView we have to map views to  url Manually  but in ViewSET we donot need to map any view routes will automatically map the views to url.
class TestAPIView(APIView) :

    def get (self , request , *args, **kwargs): 

        colors = ['red' , 'blue' , 'green' , 'yellow']

        # Response is responsiable to convert p-dict to json
        return Response({'msg' :'happy pongal', 'colors' : colors })
    
    def post(self , request , *args , **kwargs) :

        serializer = NameSerializer(data = request.data)
        
        # if valdation is ok
        if serializer.is_valid() :
            # print(serializer.data)
            name = serializer.data.get('name')

            msg = f"hello {name} ,Happy pongal !!"

            return Response({'msg' : msg})
        
        # if any valdations fails
        else :
            return Response(serializer.errors , status = 400)
        
    def put(self , request , *args , **kwargs):

        return Response({'msg' : "This is from put method"})
    
    def patch(self , request , *args , **kwargs):

        return Response({'msg' : "This is from patch method"})
    
    def delete(self , request , *args , **kwargs):

        return Response({'msg' : "This is from delete method"})
    
class TestViewSet(ViewSet) :
    # Read
    def list(self , request) : 

        colors = ['red' , 'blue' , 'green' , 'yellow']

        return Response({'msg' :'happy pongal', 'colors' : colors })
    
    # post
    def create(self , request) :

        serializer = NameSerializer(data = request.data)
        
        # if valdation is ok
        if serializer.is_valid() :
            # print(serializer.data)
            name = serializer.data.get('name')

            msg = f"hello {name} ,Happy pongal !!"

            return Response({'msg' : msg})
        
        # if any valdations fails
        else :
            return Response(serializer.errors , status = 400)
    # Only want a particular record 

    def retrieve(self , request , pk = None):

        return Response({"msg" : "This response is from retrive method for ViewSet"})
    
    def update(self , request , pk = None):

        return Response({"msg" : "This response is from upadte method for ViewSet"})

    def partial_update(self , request , pk = None):

        return Response({"msg" : "This response is from partial update method for ViewSet"})
    
    def destroy(self , request , pk = None):

        return Response({"msg" : "This response is from destroy method for ViewSet"})