from django.db import models

# Model for School
class School(models.Model):
    
    Sc_Name = models.CharField(max_length=100)
    Sc_Principle = models.CharField(max_length=100)
    Sc_Location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Sc_Name
    
    
# Model for Techers
class Teacher(models.Model):
    School = models.ForeignKey(School,on_delete=models.CASCADE)
    Tname = models.CharField(max_length=100)
    T_Exp = models.IntegerField()
    type=(
        ('Python','Python'),
        ('Django','Django'),
        ('MYSQL','MYSQL'),
        ('JavaScript','Javascript'),
    )
    T_Sub = models.CharField(max_length=50,choices=type)
    
    def __str__(self):
        return self.Tname
    

# Model for Students
class Student(models.Model):
    
    School = models.ForeignKey(School,on_delete=models.CASCADE)
    Teachers = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    Sname = models.CharField(max_length=100)
    S_F_name = models.CharField(max_length=100)
    Phone_No = models.IntegerField()
    Email = models.EmailField()
    Address = models.TextField()
    
    def __str__(self):
        return self.Sname


    


 
