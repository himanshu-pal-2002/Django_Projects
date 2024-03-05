from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from .utils import analyze_sentiment
from rest_framework import status

class CommentView(APIView):
    def get(self,request):
        Cobj = Comment.objects.all()
        sobj = CommentSerializer(Cobj,many=True)
        return Response(sobj.data,status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment_text = serializer.validated_data['text']
            sentiment_result = analyze_sentiment(comment_text)
            sentiment = sentiment_result['label']

            if sentiment == 'NEGATIVE':
                # This is where you could integrate a more complex notification system
                print(f"Alert: Negative comment detected! Comment: {comment_text}")
            else:
                print(f"Alert: Positive comment detected! Comment: {comment_text}")

            serializer.save()

            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

