from rest_framework import serializers
from app.models import *

# Used ModelSerializer:
class SchoolModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
