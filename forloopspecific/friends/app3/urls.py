from app3.views import *
from django.urls import path

app_name='Aman'

urlpatterns=[
    path('Aman/',Aman,name='Aman'),
]