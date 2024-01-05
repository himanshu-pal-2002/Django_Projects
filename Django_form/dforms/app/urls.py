from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name='Home'),
    path('school/',school,name='school'),
    path('SchoolData/',SchoolData,name='SchoolData'),
    path('teacher/',teacher,name='teacher'),
    path('TeacherData/',TeacherData,name='TeacherData'),
    path('student/',student,name='student'),
    path('StudentData/',StudentData,name='StudentData'),
]

