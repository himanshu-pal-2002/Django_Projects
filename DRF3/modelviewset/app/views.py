from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.models import *
from app.serializers import *

class ProductCrud(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializers

