from django.shortcuts import render
from app.serializers import ProductModelSerializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app.models import *

class ProductCrud(ViewSet):
    def list(self,request):
        LPO = Product.objects.all()
        JPO = ProductModelSerializers(LPO,many=True)
        return Response(JPO.data)
    
    def retrive(self,request,pk):
        PO = Product.objects.get(pk=pk)
        PMO = ProductModelSerializers(PO)
        return Response(PMO.data)



