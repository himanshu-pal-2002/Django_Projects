from app1.views import *
from django.urls import path

app_name='am'

urlpatterns=[
    path('Himanshu/',Himanshu,name='Himanshu'),
]