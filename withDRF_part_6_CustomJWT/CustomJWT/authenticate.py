# all the authentication class  are child classes of BaseAuthentication
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        
        username = request.GET.get('username')

        if username is None :

            return None 
        try : 

            user = User.objects.get(username=username)
        except User.DoesNotExist :

            raise AuthenticationFailed("Your credentials are invalid.")
        return (user , None)

  
class CustomAuthenticationBasedOnCondition(BaseAuthentication):

    # Overriding authenticate method based on some conditions 

    '''
    condition 1 = len of key should be 7
    condition 2 = last character of username and first character of key should be same and lowecase
    condition 3 = Third character of key should be (Z) 
    condition 4 = Fifth character of key and first character of username should be equal
    
    '''
    def authenticate(self, request):
        
        username = request.GET.get('username')
        key = request.GET.get('key')
        
        if username is None or key is None:

            return None 
        
        condition_1 = len(key) == 7
        condition_2 = key[0] == username[-1].lower()
        condition_3 = key[2] == 'Z'
        condition_4 = key[4] == username[0]

        #  root  tXZXr89 
        '''Handling error if user not found in database'''
        try : 

            user = User.objects.get(username=username)
        except User.DoesNotExist :

            raise AuthenticationFailed("Your credentails are invalid.")
        
        '''Checking all the condtion for user authencation'''
        if  condition_1 and condition_2 and condition_3 and condition_4 :

            return (user, None)
        
        raise AuthenticationFailed("Your provided key is invalid.")


# http://127.0.0.1:8000/api/?username=root&key=tXZXr89
