from rest_framework import viewsets
from .serializers import CommentCRUDSerializer
from .models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentCRUDSerializer
    queryset = Comment.objects.all()

