from django import forms


class SchoolForm(forms.Form):
    
    Sc_Name = forms.CharField()
    Sc_Principle = forms.CharField()
    Sc_Location = forms.CharField()

class TeacherForm(forms.Form):
    pass

class StudentForm(forms.Form):
    pass
    


