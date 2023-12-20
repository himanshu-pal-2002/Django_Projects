from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=50)
    Designation=models.CharField(max_length=50)
    Email=models.EmailField()
    Company_Name=models.CharField(max_length=40)
    