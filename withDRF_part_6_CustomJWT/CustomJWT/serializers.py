from rest_framework.serializers import ModelSerializer
from CustomJWT.models import AJIO

class AJIOSerializer(ModelSerializer):

    class Meta : 
        model = AJIO

        fields = '__all__'