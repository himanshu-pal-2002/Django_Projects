from django.db import models

# Create School Models.
class School(models.Model):
    
    School_Name = models.CharField(max_length=100)
    School_Location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.School_Name