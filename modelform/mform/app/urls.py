from django.urls import path
from .views import *

urlpatterns = [
    path('',school,name='school'),
    path('teacher/',teacher,name='teacher'),
]
