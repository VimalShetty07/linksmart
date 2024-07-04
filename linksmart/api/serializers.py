from rest_framework import serializers
from .models import Employee,Manager,Department



class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'



class ManagerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'



class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'