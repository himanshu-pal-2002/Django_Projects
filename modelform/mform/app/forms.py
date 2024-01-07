from django import forms
from .models import School,Teacher


class schoolform(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
    
    
class teacherform():
    class Meta:
        model = Teacher
        fields = '__all__'