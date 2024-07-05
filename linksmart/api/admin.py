from django.contrib import admin
from .models import Employee,Manager,Department

# Register your models here.
admin.site.register(Department)
admin.site.register(Manager)
admin.site.register(Employee)