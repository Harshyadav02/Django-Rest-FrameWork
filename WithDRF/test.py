import requests 
import json
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = "singleapi/"

def get_response(id = None):

    data = {}

    if id is not None: 
        data= {
            'id': id,
        }

    resp = requests.get(BASE_URL + ENDPOINT,  data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())

def create_emp() :

    new_emp = {
        'eno' : 700,
        'ename' : 'Dadaji',
        'esal' : 500,
        'eaddr' : 'banganga',
    }

    resp = requests.post(BASE_URL + ENDPOINT , data = json.dumps(new_emp))    # here data is our request body 
    print(resp.status_code)
    print(resp.json())

def update_resource(id) :

    new_emp = {
        'id' : id,
        
        'esal' : 500002,
        
    }

    resp = requests.put(BASE_URL + ENDPOINT, data = json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())

def delete_resource(id =None) :
    data = {}
    if id is not None :
        data = {
            'id' : id,
        }
    resp = requests.delete(BASE_URL + ENDPOINT , data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())

# get_response(4)
create_emp()
# update_resource(1)
# delete_resource(1)
    
