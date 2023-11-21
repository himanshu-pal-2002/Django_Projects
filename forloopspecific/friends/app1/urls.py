from .import views
from django.urls import path
app_name='Himanshu'

urlpatterns=[
    path('/',views.Himanshu,name='Himanshu'),
]