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

    
    def post(self,request,id):
        JDO=request.data
        PDO=ProductModelSerializers(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'Data is inserted Successfully'})
        else:
            return Response({'Error':'Data is not Inserted'})

    
