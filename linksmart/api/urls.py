from django.urls import path
from .views import EmployeeListView,ManagerListView,DepartmentListView,EmployeeAddView,DepartmentAddView,ManagerAddView,PhotoUploadView


urlpatterns = [
    path('department/', DepartmentListView.as_view(),name="department-list-view"),
    path('manager/', ManagerListView.as_view(),name="manager-list-view"),
    path('employee/', EmployeeListView.as_view(),name="employee-list-view"),
    path('add/department/', DepartmentAddView.as_view(),name="department-add-view"),
    path('add/manager/', ManagerAddView.as_view(),name="manager-add-view"),
    path('add/employee/', EmployeeAddView.as_view(),name="employee-add-view"),
    path('photo/upload', PhotoUploadView.as_view(),name="employee-add-view"),
]