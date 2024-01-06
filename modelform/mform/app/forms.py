from django import forms
from .models import School


class schoolform(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
    