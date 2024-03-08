from rest_framework import serializers
from app.models import *

# Serializers for Product Model:
class ProductModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'