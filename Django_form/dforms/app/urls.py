from django.urls import path
from .views import *

urlpatterns = [
    path('',school,name='school'),
    path('SchoolData/',SchoolData,name='SchoolData'),
    path('teacher/',teacher,name='teacher'),
    path('student/',student,name='student'),
]

