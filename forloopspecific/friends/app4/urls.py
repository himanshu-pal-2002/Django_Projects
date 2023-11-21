from app4.views import *
from django.urls import path

app_name='Vidhan'

urlpatterns=[
    path('Vidhan/',Vidhan,name='Vidhan'),
]