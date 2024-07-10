from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employee,Department,Manager
from .serializers import EmployeeListSerializer,DepartmentListSerializer,ManagerListSerializer
from rest_framework.response import Response
from PIL import Image
from rest_framework.parsers import MultiPartParser, FormParser

import cv2 


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
        



class PhotoUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('image')
        if not image_file:
            return Response({"detail": "No file provided"}, status=400)
        try:
            img = Image.open(image_file)
            width, height = img.size
            size = width * height
            data = {'size': size, 'width': width, 'height': height}
            return Response(data, status=201)
        except Exception as e:
            return Response({"detail": str(e)}, status=400)




        
# class PhotoUploadView(APIView):
#     def post(self, request):
#         image_file = request.FILES['image']

        # cv2
        # img = cv2.imread("geeksforgeeks.png") 
        # wid = img.shape[1] 
        # hgt = img.shape[0] 
        
        # print(str(wid) + "x" + str(hgt))
        # with Image.open(image_file) as img:
        #     size = img.size[0] * img.size[1]  # Width * Height in pixels
        #     width, height = img.size

            # No need to save the image, return data directly
            # data = {'size': size, 'width': width, 'height': height}
        # img = Image.open(image_file) 
        # wid, hgt = img.size 
        # print(wid,hgt)
        # return Response("data", status=201)