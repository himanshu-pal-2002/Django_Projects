from django.db import models
from django.urls import reverse

# Model for Schools:
class School(models.Model):

    sname  = models.CharField(max_length=100)
    sprincipal  = models.CharField(max_length=100)
    slocation  = models.CharField(max_length=100)


    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})


    def __str__(self):
        return self.sname

# Model for Students.  
class Student(models.Model):

    sname  = models.CharField(max_length=100)
    sage  = models.IntegerField()
    Sname = models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return self.sname





