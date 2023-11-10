"""
URL configuration for multiapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mi.views import *
from rcb.views import *
from csk.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Rohit/',Rohit,name='Rohit'),
    path('Bumrah/',Bumrah,name='Bumrah'),
    path('Virat/',Virat,name='Virat'),
    path('Abd/',Abd,name='Abd'),
    path('Msd/',Msd,name='Msd'),
    path('Raina/',Raina,name='Raina'),
    
    
    
    
]
