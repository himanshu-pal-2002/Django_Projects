from django.db import models

# Create Model for School:
class School(models.Model):

    sname  = models.CharField(max_length=100)
    sprincipal  = models.CharField(max_length=100)
    slocation  = models.CharField(max_length=100)

    def __str__(self):
        return self.sname

# Create model for Students.
    
class Student(models.Model):

    sname  = models.CharField(max_length=100)
    sage  = models.IntegerField()
    Sname = models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')


    def __str__(self):
        return self.sname





