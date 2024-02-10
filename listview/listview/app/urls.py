from django.urls import path
from .views import *

urlpatterns = [
    path('',list.as_view(),name='list'),
    path('(?P<pk>\d+)/',SchoolDetail.as_view(),name='detail'),
]