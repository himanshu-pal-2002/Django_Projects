from django.db import models

# Create Models for Students:
class Student(models.Model):

    sname  = models.CharField(max_length=100)
    smob = models.IntegerField()

    def __str__(self):
        return self.sname

