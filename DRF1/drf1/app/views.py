from django.shortcuts import render
from rest_framework.response import Response
from app.serializers import *
from rest_framework.decorators import APIView

# Create Views For CRED by using API views:
class ProductCred(APIView):
    # For getting the Data:
    def get(self,request,id):
        PDO = Product.objects.all()
        SDO = ProductModelSerializers(PDO, many=True)
        return Response(SDO.data)
    
