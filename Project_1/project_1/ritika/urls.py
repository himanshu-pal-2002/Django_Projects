from .import views
from django.urls import path

urlpatterns=[
    path('Sammy',views.Sammy,name='Sammy'),
]