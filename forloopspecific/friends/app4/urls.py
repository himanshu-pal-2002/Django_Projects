from app4.views import *
from django.urls import path

app_name='om'

urlpatterns=[
    path('Vidhan/',Vidhan,name='Vidhan'),
]