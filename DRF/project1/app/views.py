from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Views For API View for GET AND POST Data:
@api_view(['GET','POST'])
def School_Json_Data(request):
    SOD = School.objects.all()
    JOD = SchoolModelSerializer(SOD, many=True)
    Jsondata = JOD.data

    return Response(Jsondata)


