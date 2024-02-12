from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('',list.as_view(),name='list'),
    re_path('(?P<pk>\d+)/',SchoolDetail.as_view(),name='detail'),
]