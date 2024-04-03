from rest_framework import serializers
from DRF.models import Employee

# Below code is for normal serializer in the code we have manully created the create and update methods we have manully defined the fields 
def multiples_of_1000(value):

    if value % 1000 != 0:

        raise serializers.ValidationError('Salary should be multiples of 1000s')
class EmployeeSerializer(serializers.Serializer):

    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=64)
    esal = serializers.FloatField(validators=[multiples_of_1000,])
    eaddr = serializers.CharField(max_length=64)
    
    # To perform Post opertion we have to override create method
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    # to perform put operations we have to override update method
    def update(self, instance, validated_data):
        
        '''Two parameters will be passed instance and validated_data. The instance parameter represents the instance of the model that is being updated. In other words, it refers to the existing object in the database and validated_data is a JSON containing the updated field values provided by the user or client. '''
                
        instance.eno = validated_data.get('eno' , instance.eno)
        instance.ename = validated_data.get('ename' , instance.ename)
        instance.esal = validated_data.get('esal' , instance.esal)
        instance.eaddr = validated_data.get('eaddr' , instance.eaddr)
        instance.save() 
        return instance
    
    # field level validation  in field level only one key is required for validation 

    # def validate_esal (self, value) :

    #     if value < 5000 :

    #         raise serializers.ValidationError("Employee salary should be minimum 5000")
    #     return value
    
    # # object level validation in object level there are more then 1 keys for validation
    # def validate(self, data):
        
    #     ename = data.get('ename')
    #     esal = data.get('esal')

    #     if ename.lower() == "sunny" :

    #         if esal < 50000 :

    #             raise serializers.ValidationError("Sunny salary should be greater then 50000")
    #     return data



# Model serializer These are same as Model form we have to defin a meta class inside it and a field varible we do not have to define update and create method explacitly Model serializer will take care of it


# class EmployeeSerializer(serializers.ModelSerializer) :

#     class Meta : 

#         model = Employee

#         fields = '__all__'