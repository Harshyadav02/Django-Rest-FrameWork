from rest_framework.serializers import ModelSerializer
from Pagination.models import AJIO

class AJIOSerializer(ModelSerializer):

    class Meta : 
        model = AJIO

        fields = '__all__'

