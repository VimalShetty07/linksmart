from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Manager(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,null=True,blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,null=True,blank=True)
    salary  = models.IntegerField(null=True,blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

    

