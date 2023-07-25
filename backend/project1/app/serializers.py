from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'



    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.name=validated_data.get("name",instance.name)
        instance.rollno=validated_data.get("rollno",instance.rollno)
        instance.address=validated_data.get("address",instance.address)
        instance.save()
        return instance