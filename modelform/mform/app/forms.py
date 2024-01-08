from django import forms
from .models import School,Teacher


class schoolform(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
    
    
class teacherform(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        # exclude = ['texp']
        # labels = {'texp':'Teacher Experience'}
        # widgets = {'texp':forms.PasswordInput()}