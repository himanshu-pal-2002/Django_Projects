from django.db import models

# Create Models for School:
class School(models.Model):

    scname = models.CharField(max_length=100)
    scprincipal = models.CharField(max_length=100)
    sclocation = models.CharField(max_length=100)

    def __str__(self):
        return self.scname



