from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employee,Department,Manager
from .serializers import EmployeeListSerializer,DepartmentListSerializer,ManagerListSerializer
from rest_framework.response import Response

# Create your views here.
class DepartmentListView(APIView):
    def get(self, request):
        department_list = Department.objects.all()
        serializer = DepartmentListSerializer(department_list, many=True)
        return Response(serializer.data)

class ManagerListView(APIView):
    def get(self, request):
        manager_list = Manager.objects.all()
        serializer = ManagerListSerializer(manager_list, many=True)
        return Response(serializer.data)

class EmployeeListView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeListSerializer(employees, many=True)
        return Response(serializer.data)
    

class DepartmentAddView(APIView):
    def post(self, request):
        serializer = DepartmentListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

class ManagerAddView(APIView):
    def post(self, request):
        serializer = ManagerListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

class EmployeeAddView(APIView):
    def post(self, request):
        serializer = EmployeeListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)