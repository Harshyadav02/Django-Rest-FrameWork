from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User


'''
    This class implements authentication based on four conditions 
    There are four getter and for setter methods for each condition
    authenticate method is the actual method which implements the authentication
'''
class CustomAuthenticationBasedOnCondition(BaseAuthentication):

    '''
    condition 1 = length of key should be 7
    condition 2 = last character of username and first character of key should be same and lowecase
    condition 3 = Third character of key should be (Z) 
    condition 4 = Fifth character of key and first character of username should be equal
    
    '''
    def __init__(self):
        self._condition_1 = False
        self._condition_2 = False
        self._condition_3 = False
        self._condition_4 = False

    @property
    def condition_1(self):
        return self._condition_1

    @condition_1.setter
    def condition_1(self, value):
        self._condition_1 = value

    @property
    def condition_2(self):
        return self._condition_2

    @condition_2.setter
    def condition_2(self, value):
        self._condition_2 = value

    @property
    def condition_3(self):
        return self._condition_3

    @condition_3.setter
    def condition_3(self, value):
        self._condition_3 = value

    @property
    def condition_4(self):
        return self._condition_4

    @condition_4.setter
    def condition_4(self, value):
        self._condition_4 = value

    # Overriding authenticate method based on the  conditions 

    def authenticate(self, request):
        username = request.GET.get('username')
        key = request.GET.get('key')

        if username is None or key is None:
            return None

        self.condition_1 = len(key) == 7
        self.condition_2 = key[0] == username[-1].lower()
        self.condition_3 = key[2] == 'Z'
        self.condition_4 = key[4] == username[0]

        # Handling error if username is not valid
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed("Your credentials are invalid.")

        if self.condition_1 and self.condition_2 and self.condition_3 and self.condition_4:
            return (user, None)

        raise AuthenticationFailed("Your provided key is invalid.")

# http://127.0.0.1:8000/api/?username=root&key=tXZXr89
