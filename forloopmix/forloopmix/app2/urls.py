from django.urls import path
from app2.views import *

app_name='hai'

urlpatterns=[
    path('Aditya/',Aditya,name='Aditya'),
    path('Vidhan/',Vidhan,name='Vidhan'),
    
]