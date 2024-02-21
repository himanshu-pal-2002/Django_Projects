# vehicles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicle_list, name='vehicle_list'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
]
