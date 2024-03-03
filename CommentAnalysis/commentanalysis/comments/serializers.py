from rest_framework import serializers
from .models import Comment

# Class For CommentSerializer:
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at']
