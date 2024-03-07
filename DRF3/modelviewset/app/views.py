from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.models import *
from app.serializers import *

# Views for Product Crud Operation by using ModelViewSet:
class ProductCrud(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializers

