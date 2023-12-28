from django.db import models

# Create your models here.
class Introduction(models.Model):
    Name = models.CharField(max_length=100)
    type = (
        ('PG','PG'),
        ('UG','UG'),
    )
    Education = models.CharField(max_length=50,choices=type)
    Address = models.CharField(max_length=100)
    Phone_No = models.IntegerField()
    Email = models.EmailField()
    
    def __str__(self):
        return self.Name