from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser

from DRF.serializers import EmployeeSerializer
from DRF.models import Employee

import io

@method_decorator(csrf_exempt , name="dispatch")
class EmployeeCRUDCBV(View) :

    def get(self, request, *args, **kwargs):

        json_data = request.body      # retrving data sent by app

        # conversion of json data into python dictionary
        stream = io.BytesIO(json_data) # This line  converts the JSON data to a binary stream.
        p_data = JSONParser().parse(stream)  # parses that binary stream as JSON and converts it to a Python data structure.

        # retriving id if sent form patner application i.e need info for a specific employee
        id = p_data.get('id' , None)

        if id is not None :

            emp = Employee.objects.get(id = id)  # retrving a single employee based on id
            print((emp.id))
            # converting python dict to json
            serializer = EmployeeSerializer(emp) 
            json_data = JSONRenderer().render(serializer.data)

            return HttpResponse(json_data ,content_type = 'application/json' )

        # if id is none then we have to send all data i.e querySet

        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs, many =True)
        json_data = JSONRenderer().render(serializer.data)

        return HttpResponse(json_data ,content_type = 'application/json' )

    def post(self, request, *args, **kwargs):

        json_data  = request.body

        # converting json to py-dict
        stream = io.BytesIO(json_data) 
        pdata = JSONParser().parse(stream)
        print(type(pdata))
        serializer = EmployeeSerializer(data = pdata) # passing dictionary to Serializer class so that it can be conveted to obejct and can be stored to database

        if serializer.is_valid():
            serializer.save()
            msg = {'msg' : "Resource Created Sucessfully"}
            json_data = JSONRenderer().render(msg)

            return HttpResponse(json_data ,content_type = 'application/json' )

        json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data ,content_type = 'application/json' , status= 400)


    def put(self, request, *args, **kwargs):

        json_data = request.body
        
        # Json to py-dict
        stream = io.BytesIO(json_data)
        p_data = JSONParser().parse(stream)

        id = p_data.get('id', None)
        emp = Employee.objects.get(id = id)
        serializer = EmployeeSerializer(emp , data = p_data, partial = True)
        
        if serializer.is_valid(): 
            serializer.save()

            msg = {'msg' : "Resource Updated Sucessfully"}
            json_data = JSONRenderer().render(msg)

            return HttpResponse(json_data ,content_type = 'application/json' )

        json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data ,content_type = 'application/json' , status= 400)
    
    def delete(self, request , *args,**kwargs):

        json_data = request.body
        # Json to py-dict
        stream = io.BytesIO(json_data)
        p_data = JSONParser().parse(stream)

        id = p_data.get('id', None)
        emp = Employee.objects.get(id = id)
        emp.delete()

        msg = {'msg' : "Resource Deleted Sucessfully"}
            
        json_data = JSONRenderer().render(msg)

        return HttpResponse(json_data ,content_type = 'application/json' )