from django.urls import path
from .import views

urlpatterns = [
    path('',views.Login_Page,name='Login_Page'),
]
