from django.shortcuts import render
from django.http import HttpResponse
from api.models import Employee,Department,Manager

# Create your views here.
def home(request):
    employees_list = Employee.objects.all()
    department_list = Department.objects.all()
    manager_list = Manager.objects.all()
    return render(request, 'home.html' , {"employees": employees_list,"department": department_list,"manager": manager_list})