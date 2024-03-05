from django.shortcuts import render
from requests import Response
from app.models import *
from app.serializers import ProductModelSerializers
from rest_framework.decorators import APIView

# Create Views For CRED by using API views:
class ProductCred(APIView):
    def get(self,request):
        PDO = Product.objects.all()
        SDO = ProductModelSerializers(PDO,many=True)
        return Response(SDO.data())
