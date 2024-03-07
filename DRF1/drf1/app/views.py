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

    # For inserting the Data:
    def post(self,request,id):
        PDO = request.data
        SDO = ProductModelSerializers(data=PDO)
        if SDO.is_valid():
            SDO.save()
            return Response({'insert':'Data is inserted Successfully'})
        else:
            return Response({'Error':'Data is not Inserted'})

    
    # def put(self,request,id):
    #     PO=Product.objects.get(id=id)
    #     UPDO=ProductModelSerializers(PO,data=request.data)
    #     if UPDO.is_valid():
    #         UPDO.save()
    #         return Response({'update':'Data is Updated'})
    #     else:
    #         return Response({'error':'Update not done'})
    
    # def patch(self,request,id):
    #     PO=Product.objects.get(id=id)
    #     UPDO=ProductModelSerializers(PO,data=request.data,partial=True)
    #     if UPDO.is_valid():
    #         UPDO.save()
    #         return Response({'update':'Data is Updated'})
    #     else:
    #         return Response({'error':'Update not done'})

    # def delete(self,request,id):
    #     Product.objects.get(id=id).delete()
    #     return Response({'deletion':'Data is Deleted'})

    
