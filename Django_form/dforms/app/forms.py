from django import forms
from .models import School,Teacher
from django.core import validators


# For Validation Purpose:
def validate_for_Sname(data):
    if len(data)<5:
        raise forms.ValidationError('length is less than 5')
        
    



class SchoolForm(forms.Form):
    
    # Sc_Name = forms.CharField()
    Sc_Name = forms.CharField(validators=[validate_for_Sname,validators.MinLengthValidator(5)])
    
    Sc_Principle = forms.CharField()
    Sc_Location = forms.CharField()

class TeacherForm(forms.Form):
    
    School=forms.ModelChoiceField(queryset=School.objects.all(),initial=0)
   
    Tname = forms.CharField(validators=[validate_for_Sname,validators.MinLengthValidator(5)])
    
    T_Exp=forms.IntegerField()
    
    s=[['Python','Python'],['Django','Django'],['MYSQL','MYSQL'],['JavaScript','JavaScript']]
    
    T_Sub=forms.ChoiceField(choices=s)
    

    
class StudentForm(forms.Form):
    
    School=forms.ModelChoiceField(queryset=School.objects.all(),initial=0)
    Teachers=forms.ModelChoiceField(queryset=Teacher.objects.all(),initial=0)
    Sname = forms.CharField(validators=[validate_for_Sname,validators.MinLengthValidator(5)])
    S_F_name = forms.CharField()
    Phone_No = forms.IntegerField()
    Email = forms.EmailField()
    Address = forms.CharField()


