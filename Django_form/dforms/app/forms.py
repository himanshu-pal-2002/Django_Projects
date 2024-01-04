from django import forms
from .models import School,Teacher


class SchoolForm(forms.Form):
    
    Sc_Name = forms.CharField()
    Sc_Principle = forms.CharField()
    Sc_Location = forms.CharField()

class TeacherForm(forms.Form):
    
    School=forms.ModelChoiceField(queryset=School.objects.all(),initial=0)
    Tname=forms.CharField()
    T_Exp=forms.IntegerField()
    
    s=[['Python','Python'],['Django','Django'],['MYSQL','MYSQL'],['JavaScript','JavaScript']]
    
    T_Sub=forms.ChoiceField(choices=s)
    

class StudentForm(forms.Form):
    
    School=forms.ModelChoiceField(queryset=School.objects.all(),initial=0)
    Teachers=forms.ModelChoiceField(queryset=Teacher.objects.all(),initial=0)
    Sname = forms.CharField()
    S_F_name = forms.CharField()
    Phone_No = forms.IntegerField()
    Email = forms.EmailField()
    Address = forms.CharField()


